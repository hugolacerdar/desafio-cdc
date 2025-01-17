import asyncio
import sys
from subprocess import PIPE, STDOUT

cleanup_called = False


async def run_command(command: str, description: str) -> None:
	"""Run a shell command and handle stdout/stderr (streamed line by line)."""
	print(f'\n⏳ {description}...')
	process = await asyncio.create_subprocess_shell(
		command,
		stdout=PIPE,
		stderr=STDOUT,
	)
	try:
		# Stream output in real-time
		while True:
			line = await process.stdout.readline()  # type: ignore
			if not line:
				break
			print(line.decode().rstrip())

		# Wait for the process to finish and check for errors
		return_code = await process.wait()
		if return_code == 0:
			print(f'\n✅ Success: {description}')
		else:
			raise RuntimeError(f'{description} failed with exit code {return_code}')
	except Exception:
		process.kill()
		await process.wait()
		raise


async def cleanup() -> None:
	"""Cleanup resources by stopping services."""
	global cleanup_called
	if cleanup_called:
		return
	cleanup_called = True

	print('\n🧹 Cleaning up resources...')
	try:
		await run_command('make services-stop', 'Stopping services')
		print('\n✅ Cleanup completed successfully!')
	except Exception as e:
		print(f'\n❌ Cleanup script failed: {e}')


async def start_dev_server() -> None:
	"""
	Start the development server in the foreground (stdout=None/stderr=None),
	so logs appear immediately. We'll wait until the server exits.
	"""
	print('\n🚀 Starting the development server...\n')
	dev_server = await asyncio.create_subprocess_exec(
		'poetry',
		'run',
		'python',
		'main.py',
		stdout=None,  # Inherit Python’s stdout
		stderr=None,  # Inherit Python’s stderr
	)

	# Wait for the dev server to exit
	return_code = await dev_server.wait()
	print(f'\n🚀 Dev server exited with code {return_code}. Triggering cleanup...')
	await cleanup()


async def main() -> None:
	try:
		# 1. Start services
		await run_command('make services-up', 'Starting necessary services...')

		# 2. Wait for database
		await run_command('make services-wait-db', 'Waiting for the database to become available...')

		# 3. Start the dev server and block until it exits
		await start_dev_server()

	except Exception as e:
		print('\n💥 An error occurred during the dev setup:')
		print(e)
		await cleanup()


def run_dev_env_manager() -> None:
	"""
	Runs the async environment manager with graceful KeyboardInterrupt handling.
	"""
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('\n⚡ Received KeyboardInterrupt. Initiating cleanup...')
		loop = asyncio.new_event_loop()
		try:
			loop.run_until_complete(cleanup())
		finally:
			loop.close()
		sys.exit(0)
	except Exception as e:
		print(f'\nUnexpected error: {e}')
		sys.exit(1)


if __name__ == '__main__':
	run_dev_env_manager()
