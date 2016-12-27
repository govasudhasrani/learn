
import asyncio

@asyncio.coroutine
def fun1():
    print("Starting fun1")
    result = yield from fun2()
    print("Ended with result ", result)

@asyncio.coroutine
def fun2():
    print("Starting fun2")
    result = yield from fun3()
    print("Ended with result ", result)
    return result + 1

@asyncio.coroutine
def fun3():
    print("Starting and ending from fun3")
    return 1


@asyncio.coroutine
def task_runner(id, time_to_wait):
    print("Started task ", id)
    yield from asyncio.sleep(time_to_wait)
    print("End task ", id)



if __name__  == "__main__":

 #   event_loop = asyncio.get_event_loop()
 #   event_loop.run_until_complete(fun1())
 #   event_loop.close()

    tasks = [task_runner(1, 5), task_runner(2, 10), task_runner(3, 2)]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.wait(tasks))
    event_loop.close()

# good reads:
# http://www.andy-pearce.com/blog/posts/2016/Jun/the-state-of-python-coroutines-introducing-asyncio/
# http://www.giantflyingsaucer.com/blog/?p=5557
# http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/
# https://pymotw.com/3/asyncio/concepts.html
# http://www.drdobbs.com/open-source/the-new-asyncio-module-in-python-34-even/240168401