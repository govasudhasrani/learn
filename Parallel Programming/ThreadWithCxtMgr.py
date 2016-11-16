import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                   format='(%(threadName)s) %(message)s',)


def thread_with_context_mgr(lock_instance):
    with lock_instance:
        logging.debug("Message from thread in context manager and lock " + str(lock_instance))

def thread_without_context_mgr(lock_instance):
    lock_instance.acquire()
    try:
        logging.debug("Message from thread without context manager. Here lock is " + str(lock_instance))
    except:
        lock_instance.release()

if __name__ == "__main__":

    lock_instances = [threading.Lock(), threading.RLock(), threading.Condition(), threading.Semaphore(1)]

    for lock in lock_instances:
        t1 = threading.Thread(target=thread_with_context_mgr, args=(lock,))
        t2 = threading.Thread(target=thread_without_context_mgr, args=(lock,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

