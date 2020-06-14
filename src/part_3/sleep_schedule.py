# -*- encoding: utf-8 -*-
# !/usr/bin/python
"""
@File    : sleep_schedule.py
@Time    : 2020/6/14 9:23
@Author  : haishiniu
@Software: PyCharm
"""
import asyncio
import asyncio.coroutines

def _set_result_unless_cancelled(fut, result):
    if fut.cancelled():
        return
    print("this is a rewrited sleep callback function")
    fut.set_result(result)

# asyncio.sleep()函数的实现版本
@asyncio.coroutine
def dalong_sleep(delay, result=None, *, loop=None):
    """Coroutine that completes after a given time (in seconds)."""
    if delay == 0:
        yield
        return result

    future = loop.create_future()
    h = future._loop.call_later(delay,
                                _set_result_unless_cancelled,
                                future, result)
    try:
        return (yield from future)
    finally:
        h.cancel()

async def cor1():
    await dalong_sleep(1, loop = event_loop)
    print("this coroutine cor1")

def call_back(res):
    print("this is cor1's callback fucntion")
# 获得一个事件循环
event_loop = asyncio.get_event_loop()
# 创建一个任务，并将任务加入事件循环
task = event_loop.create_task(cor1())
# 给任务添加回调函数
task.add_done_callback(call_back)
# 开始执行任务直到结束
event_loop.run_until_complete(task)