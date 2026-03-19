import aiohttp
import asyncio


async def fetch_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def fetch_multiple(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:

        tasks = [session.get(url) for url in urls]

        responses = await asyncio.gather(*tasks)

        html_list = []

        for r in responses:
            html_list.append(await r.text())

        return html_list