import multiprocessing

"""
child process created imports the script file where the target function is contained. Then, by instantiating the process
object within this block, we prevent an infinite recursive call of such instantiations. A valid workaround is used to
define the target function in a different script, and then imports it to the namespace.
"""
import multiprocess_target

from time import sleep

def separated_process_func(input):
    print "This message is from ", multiprocessing.current_process().name
    sleep(3)
    print "Exiting by", multiprocessing.current_process().name


class CustomProcess(multiprocessing.Process):

    def run(self):
        separated_process_func("This is another method")


if __name__ == "__main__":

    for i in range(10):
        process = multiprocessing.Process(target=multiprocess_target.target_function, args=(i,))
        process.start()

        # Without p.join(), the child process will sit idle and not be terminated, and then, you must manually kill it.
        process.join()

    process_with_name = multiprocessing.Process(name='child_process', args=("Vasudha",), target=separated_process_func)
    # Make it is as daemon process
    #process_with_name.daemon = True

    process_without_name = multiprocessing.Process(target=separated_process_func, args=("Test",))
    print "Current process name is ", multiprocessing.current_process().name

    process_with_name.start()
    process_without_name.start()


    # Testing possible monitor functionalities with multiprocessing

    process = multiprocessing.Process(target=separated_process_func, args=("Hello"))
    print "ATTEMPT1 Does process started before start... ", process, process.is_alive()
    process.start()
    print "ATTEMPT2 process status after start... ", process, process.is_alive()
    process.terminate()
    print "ATTEMPT3 process status after terminate started... ", process, process.is_alive()
    process.join()
    print "ATTEMPT4 process status after join ... ", process, process.is_alive()
    print "Find the process exit code ... ", process, process.exitcode

    #another way of process creation
    process = CustomProcess()
    process.start()
    print "Attempt... ", process, process.is_alive()
    process.join()
    print "Another attempt... ", process, process.is_alive()