import asyncio

async def start_stronman(name, power):
    print(f"Силач {name} начал соревнования")

    for i in range(1,6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i}')

    print(f"Силач{name} закончил соревнования")

async def start_tornament():
    task1 = [start_stronman('Pasha', 3),
            start_stronman('Denis', 4),
            start_stronman('Apollon', 5)]
    await asyncio.gather(*task1)

asyncio.run(start_tornament())