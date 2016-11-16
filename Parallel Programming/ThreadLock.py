
import threading

# Global resources so that all threads in the process can access and share
shared_variable_with_lock = 0
shared_variable_without_lock = 0
shared_lock = threading.Lock()
count_range = 100000

def update_shared_variable_lock(do_addition):
    global shared_variable_with_lock
    for i in range(count_range):
        shared_lock.acquire()
        shared_variable_with_lock = shared_variable_with_lock + 1 if do_addition else shared_variable_with_lock - 1
        shared_lock.release()

def update_shared_variable_without_lock(do_addition):
    global shared_variable_without_lock
    for i in range(count_range):
        shared_variable_without_lock = shared_variable_without_lock + 1 if do_addition else shared_variable_without_lock - 1

if __name__ == "__main__":
    t1 = threading.Thread(name="incrementer with lock", target=update_shared_variable_lock, args=(True,))
    t2 = threading.Thread(name="decrementer with lock", target=update_shared_variable_lock, args=(False,))
    t3 = threading.Thread(name="incrementer without lock", target=update_shared_variable_without_lock, args=(True,))
    t4 = threading.Thread(name="decrementer without lock", target=update_shared_variable_without_lock, args=(False,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print "Shared variable with lock", shared_variable_with_lock
    print "Shared variable without lock", shared_variable_without_lock