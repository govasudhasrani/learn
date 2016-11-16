from threading import Thread, Condition
from time import sleep

items = []
condition = Condition()

class Consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global items, condition

        condition.acquire()

        if len(items) == 0:
            condition.wait()
            print "Waiting for the condition to met"

        items.pop()
        print "Notified producer on the removal. Available count: ", str(len(items))
        condition.notify()
        condition.release()



    def run(self):
        for i in range(20):
            sleep(10)
            self.consume()

class Producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global items, condition

        condition.acquire()

        if len(items) == 10:
            condition.wait()
            print "Waiting till items count become <10"

        items.append(1)
        print "Notified consumer on the addition. Available count: ", str(len(items))
        condition.notify()
        condition.release()


    def run(self):
        for i in range(20):
            sleep(5)
            self.produce()


if __name__ == "__main__":
    consumer = Consumer()
    producer = Producer()
    consumer.start()
    producer.start()
    consumer.join()
    producer.join()
