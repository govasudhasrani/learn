
from threading import Thread
from random import randint
from queue import Queue

class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            print "Taking out an element ", str(self.queue.get()), "by ", self.getName()
            self.queue.task_done()

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(100):
            item = randint(1, 256)
            self.queue.put(item)
            print "Inserting an element ", item, "by ", self.getName()

if __name__ == "__main__":
    queue = Queue()
    producer = Producer(queue)
    consumer1 = Consumer(queue)
    consumer2 = Consumer(queue)
    consumer3 = Consumer(queue)

    producer.start()
    consumer1.start()
    consumer2.start()
    consumer3.start()

    producer.join()
    consumer1.join()
    consumer2.join()
    consumer3.join()


