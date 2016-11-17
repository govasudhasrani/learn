import logging

logging.basicConfig(level=logging.INFO, format='%(process)s %(threadName)s %(message)s')


def target_function(input):
    logging.info("hello")
