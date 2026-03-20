import aiohttp
import asyncio
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]


async def fetch(session, url, semaphore):
    max_retries = 3
    base_delay = 1

    async with semaphore:
        for attempt in range(1, max_retries + 1):
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS)
                }

                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    return await response.text()

            except Exception as e:
                if attempt == max_retries:
                    return None

                delay = base_delay * (2 ** (attempt - 1))
                await asyncio.sleep(delay)

async def fetch_multiple(session, urls: list[str], concurrency: int = 5):
    semaphore = asyncio.Semaphore(concurrency)

    tasks = [
        fetch(session, url, semaphore)
        for url in urls
    ]

    return await asyncio.gather(*tasks)