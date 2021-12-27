# import asyncio
#
#
# async def main():
#     print("Hello")
#     await asyncio.sleep(5)
#     print("World")
#
#
# asyncio.run(main())
import asyncio


# async def main():
#     print("Hello")
#     task = asyncio.create_task(foo("text"))
#     print("finished")
#
#
# async def foo(text):
#     print(text)
#     await asyncio.sleep(10)
#
#
# asyncio.run(main())

async def main():
    print("Hello")
    task = asyncio.create_task(foo("text"))
    await task
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(10)


asyncio.run(main())