
import asyncio
import aiohttp
import time


async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def get_async(url, session, results):
    async with session.get(url) as response:
        i = url.split('/')[-1]
        obj = await response.text()
        results[i] = obj


async def main_http(urls):
    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)
    results = {}
    # urls = [f"http://localhost:8080/user/{i}" for i in range(1000)]

    conc_req = 40
    now = time.time()
    await gather_with_concurrency(conc_req, *[get_async(i, session, results) for i in urls])
    time_taken = time.time() - now

    print(time_taken)
    await session.close()


# asyncio.run(main_http(urls))