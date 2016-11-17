from multiprocessing import Barrier, Process, Lock
from datetime import datetime
from time import  time
import multiprocessing

def test_with_barrier(synchronizer, serializer):

    synchronizer.wait()

    with serializer:
        print "Current process: ", multiprocessing.current_process().name, " current time: ", \
              datetime.fromtimestamp(time())

def test_without_barrier():
    print "Current process: ", multiprocessing.current_process().name, " current time: ", \
        datetime.fromtimestamp(time())

if __name__ == "__main__":

    """
    Barrier: This divides a program into phases as it requires all of the
    processes to reach it before any of them proceeds. Code that is
    executed after a barrier cannot be concurrent with the code
    executed before the barrier.
    """
    count_of_processes_to_be_in_barrier = 2
    synchronizer = Barrier(count_of_processes_to_be_in_barrier)
    serializer = Lock()
    p1 = Process(target=test_with_barrier, args=(synchronizer, serializer))
    p2 = Process(target=test_with_barrier, args=(synchronizer, serializer))
    p1.start()
    p2.start()
    p1.join()
    p1.join()

    p3 = Process(target=test_without_barrier)
    p4 = Process(target=test_without_barrier)
    p3.start()
    p4.start()
    p3.join()
    p4.join()