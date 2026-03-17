import aiohttp
import asyncio


async def fetch_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()