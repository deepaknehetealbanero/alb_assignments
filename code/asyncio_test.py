import asyncio
import time


async def calc_square(numbers):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n * n}')
        print("Sleeping for 5 sec so other coroutine can run in the meanwhile")
        await asyncio.sleep(5)
        # return{n*n}


async def calc_cube(numbers):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n * n * n}')
        # await asyncio.sleep(6)
        # return {n*n*n}


def main():
    start = time.time()
    # print(start)
    numbers = [*range(2, 10, 1)]

    # Run both the coroutines concurrently
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(calc_square(numbers, )),
        loop.create_task(calc_cube(numbers, ))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()

    print('Execution Time with Async: {}'.format(end - start))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error running threads:" + str(e))
