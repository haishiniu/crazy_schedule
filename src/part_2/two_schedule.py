# -*- encoding: utf-8 -*-
# !/usr/bin/python
"""
@File    : two_schedule.py
@Time    : 2020/6/1 16:39
@Author  : haishiniu
@Software: PyCharm
"""
import asyncio
import time


# async关键字表明这是个协程
async def coroutine_A():
    print("协程A开始执行")
    print("协程A出让执行权")
    # await关键字表明主动出让执行权
    await asyncio.sleep(2)
    print("协程A重新获得执行权,并执行结束")


async def coroutine_B():
    print("协程B开始执行")
    print("协程B出让执行权")
    await asyncio.sleep(2)
    print("协程B重新获得执行权,并执行结束")


async def coroutine_C():
    while (1):
        print("由于协程A,B始终等待时钟信号，协程C执行")
        await asyncio.sleep(0.4)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    group1 = [coroutine_A(), coroutine_B()]
    group1 = asyncio.gather(*group1)
    loop.run_until_complete(asyncio.gather(group1, return_exceptions=True))
    print("程序运行时间: {}".format(time.time() - start_time))
