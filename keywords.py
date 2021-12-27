import asyncio


# async def main():
#     print("Hello")
#     await asyncio.sleep(5) # here wait for 5 sec and then run below line.
#     print("world!")
#
#
# asyncio.run(main())

async def main():
    print("Hello")
    await foo('text')
    print("finished")


async def foo(text):
    print("World!")
    await asyncio.sleep(5)


asyncio.run(main())
