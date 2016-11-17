import multiprocessing

def load_pipe(pipe):
    for i in range(5):
        pipe.send(i)
    pipe.close()

def unload_pipe(input_pipe, output_pipe):
    while True:
        try:
            value = input_pipe.recv()
            print "Value received.. ", value
            output_pipe.send(value * value)
        except EOFError:
            output_pipe.close()

if __name__ == "__main__":

    input_pipe_pair = multiprocessing.Pipe(True)
    producer = multiprocessing.Process(target=load_pipe, args=(input_pipe_pair[1],))

    output_pipe_pair = multiprocessing.Pipe(True)
    consumer = multiprocessing.Process(target=unload_pipe, args=(input_pipe_pair[1], output_pipe_pair[0]))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

