import threading
from time import sleep

class Container:
    rlock = threading.RLock()

    def __init__(self):
        self.items_count = 0

    def add_or_remove(self, item):
        Container.rlock.acquire()
        self.items_count += item
        Container.rlock.release()

    def add(self):
        Container.rlock.acquire()
        self.add_or_remove(1)
        Container.rlock.release()

    def remove(self):
        Container.rlock.acquire()
        self.add_or_remove(-1)
        Container.rlock.release()


def adder(container, items):
    for item in range(0, items):
        print "Adding 1 element"
        container.add()
        sleep(2)


def remover(container, items):
    for item in range(0, items):
        print "Removing 1 element"
        container.remove()
        sleep(2)

if __name__ == "__main__":

    box = Container()
    items = 5

    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
