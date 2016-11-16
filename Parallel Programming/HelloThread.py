from threading import Thread
from time import sleep

class SubTask(Thread):
    """
    Starting a thread by sub-classing Thread class
    """
    def __init__(self):
        Thread.__init__(self)


    def run(self):
        print "\nHello... " , self.getName()


def do_task(idx):
    """
    Example for starting a thread for running a function
    :param idx:
    :return:
    """
    print "This is invoked by Thread: ", idx
    sleep(10)

if __name__ == "__main__":
    task = SubTask()

    task.start()

    for i in range(5):
        task = Thread(target=do_task, args=(i,))
        task.start()

        # Calling thread wait for this thread to complete
        task.join()

    print "This is main ... ended"