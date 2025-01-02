import asyncio

async def hell():
    print("hello")
    await asyncio.sleep(15)
    print("world")

asyncio.run(hell())
