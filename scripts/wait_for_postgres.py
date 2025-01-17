import asyncio


async def check_postgres() -> bool:
	"""Check if PostgreSQL is ready by running pg_isready inside the container."""
	process = await asyncio.create_subprocess_shell(
		'docker exec postgres-dev pg_isready --host localhost',
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE,
	)
	stdout, _ = await process.communicate()

	# Check if the output contains "accepting connections"
	if b'accepting connections' in stdout:
		print('\n\n✅ PostgreSQL is available!\n')
		return True
	else:
		return False


async def wait_for_postgres() -> None:
	"""Wait for PostgreSQL to become available, retrying until it is ready."""
	print('🔴 Waiting for PostgreSQL to become available...', end='', flush=True)
	while True:
		ready = await check_postgres()
		if ready:
			break
		print('.', end='', flush=True)
		await asyncio.sleep(1)  # Wait 1 second before retrying


if __name__ == '__main__':
	asyncio.run(wait_for_postgres())
