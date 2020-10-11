import asyncio
import time

async def numeros():
    letras()
    for x in range(20):
        print(x)
        await letras_c()

async def letras():
    await letras_b()
    print("a")

async def letras_b():
    print("b")

async def letras_c():
    for c in range(4):
        print("c")


l = asyncio.get_event_loop()

tareas = asyncio.gather(numeros(),letras())

l.run_until_complete(tareas)