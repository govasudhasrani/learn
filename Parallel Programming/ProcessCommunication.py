import multiprocessing
import random
import time

class Producer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(1, 100)
            self.queue.put(item)
            print "Producer Process: ", self.name, " had put ", item, " to queue "
            time.sleep(1)
            print "Producer ... queue size is ", self.queue.qsize()


class Consumer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):

        while True:
            time.sleep(10)
            if self.queue.empty():
                print "Consumer. Queue is empty"
                break
            else:
                print "Consumer .. ", self.name, " Got the item .. ", self.queue.get()


if __name__ == "__main__":

    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()