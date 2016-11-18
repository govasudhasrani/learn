import multiprocessing

def do_number_square(num):
    result = num * num
    #print("Process: ", multiprocessing.current_process().name, " has given result: ", result)
    return result

def update_dict(dictionary, key, value):
    dictionary[key] = value

if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    shared_dict = mgr.dict()

    processes = [ multiprocessing.Process(target=update_dict, args=(shared_dict, i, i * i)) for i in range(6)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print shared_dict
