#! /usr/local/bin/python3

import asyncio
import time

def fun1(cutoff_time, event_loop):

    cur_time = event_loop.time()
    print("Entering function1 at ", cur_time)
    if cur_time < cutoff_time:
        event_loop.call_later(1, fun2, cutoff_time, event_loop)
    else:
        event_loop.stop()

def fun2(cutoff_time, event_loop):
    cur_time = event_loop.time()
    print("Entering function2 at ", cur_time)
    if cur_time < cutoff_time:
        event_loop.call_later(1, fun3, cutoff_time, event_loop)
    else:
        event_loop.stop()

def fun3(cutoff_time, event_loop):
    cur_time = event_loop.time()
    print("Entering function3 at ", cur_time)
    if cur_time < cutoff_time:
        event_loop.call_later(1, fun1, cutoff_time, event_loop)
    else:
        event_loop.stop()

#if __name__ == "__main__":

print("hello")

event_loop = asyncio.get_event_loop()
cutoff_time = event_loop.time() + 5
event_loop.call_soon(fun1, cutoff_time, event_loop)
event_loop.run_forever()
event_loop.close()