import concurrent.futures
import os
import time
import multiprocessing


def manipulate_num(num):
    for i in range(100000):
        i = i+1
    return i + num

def evaluate_item(num):
    result = manipulate_num(num)
    print("Result: ", result, " from process: ", multiprocessing.current_process().name)

if __name__ == "__main__":

    test_numbers = list(range(20))

    # Test with sequential execution
    start_time = time.clock()
    for i in test_numbers:
        evaluate_item(i)
    print("Completed sequential execution taking ", str(time.clock() - start_time), "seconds")

    # Test with thread pool
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in test_numbers:
            executor.submit(evaluate_item, args=(i,))
    print("Completed parallel execution with threads taking ", str(time.clock() - start_time), "seconds")

    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for i in test_numbers:
            executor.submit(evaluate_item, args=(i,))
    print("Completed parallel execution with processes taking ", str(time.clock() - start_time), "seconds")
