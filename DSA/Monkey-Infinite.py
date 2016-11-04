"""

The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount
of time will almost surely type a given text, such as the complete works of William Shakespeare. In fact the monkey
would almost surely type every possible finite text an infinite number of times. However, the probability of a universe
full of monkeys typing a complete work such as Shakespeare's Hamlet is so tiny that the chance of it occurring during a
period of time hundreds of thousands of orders of magnitude longer than the age of the universe is extremely low
(but technically not zero).
core every 1000 tries.

"""


from random import randrange

ALPHABET_CLASS = "abcdefghijklmnopqrstuvwxyz "

def random_str_generator(str_len):
    """

    :param str_len:
    :return:
    """

    rand_str = "".join(ALPHABET_CLASS[randrange(str_len)] for idx in range(str_len))

    return rand_str

def find_match_score(target_str, rand_str):
    """

    :param target_str:
    :param rand_str:
    :return:
    """
    score = 0
    for idx in range(len(target_str)):
        if rand_str[idx] == target_str[idx]:
            score = score + 1

    return float(score) / float(len(target_str))

if __name__ == '__main__':

    trial1 = random_str_generator(27)
    print("STRING is", trial1, find_match_score("EQWEQW", trial1))

