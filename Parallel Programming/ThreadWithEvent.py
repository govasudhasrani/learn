from random import randint
from threading import Thread, Event
from time import sleep


items = []
event = Event()

class Consumer(Thread):


    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event


    def run(self):
        while True:
            sleep(2)
            self.event.wait()
            print "Popping item {0} from thread".format(self.items.pop(), self.getName())

class Producer(Thread):

    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        for i in range(200):
            sleep(2)
            item = randint(1, 100)
            self.items.append(item)
            print "Added new item {0} by producer {1}".format(item, self.getName())
            self.event.set()
            print "Producer notify: setting event ", self.getName()
            self.event.clear()
            print "Producer notify: clearing event ", self.getName()

if __name__ == "__main__":
    consumer = Consumer(items, event)
    producer = Producer(items, event)

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()