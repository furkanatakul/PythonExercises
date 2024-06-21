import threading
import requests
import time
import asyncio
import aiohttp
def getDataSync(urls):
    st = time.time()
    jsonArray=[]
    for url in urls:
        jsonArray.append(requests.get(url).json())
    et = time.time()
    elapsedTime = et-st
    print("Execution time: ", elapsedTime ,"seconds")
    print(jsonArray)
    return jsonArray

class ThreadingDownloader(threading.Thread):
    jsonArray = []
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        response = requests.get(self.url)
        self.jsonArray.append(response.json())
        print(self.jsonArray)
        return self.jsonArray

def getDataThreading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "seconds")

async def getDataAsyncButAsWrapper(urls):
    st = time.time()
    jsonArray = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                jsonArray.append(await response.json())

    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "seconds")

async def getData(session,url,jsonArray):
    async with session.get(url) as response:
        jsonArray.append(await response.json())

async def getDataAsncConcurrently(urls):
    st = time.time()
    jsonArray = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(getData(session,url,jsonArray)))
        await asyncio.gather(*tasks)
    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "seconds")
    return jsonArray

urls = ["https://postman-echo.com/delay/5"] * 10
#getDataSync(urls) # 65
#getDataThreading(urls) # 5.60
#asyncio.run(getDataAsyncButAsWrapper(urls)) # 53
#asyncio.run(getDataAsncConcurrently(urls)) # 5.70
