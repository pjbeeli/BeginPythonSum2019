"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics

def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    """
    freq = [0] *6 # hexagonal die
 # empty list
    for roll in range(num):
        n = random.randrange(1,7)
        freq[n -1] += 1

    return freq


def my_code():
    """
    Test function
    :return: 
    """
#    num = int(input("How many times you need to roll"))
    num = 6000
    result = roll_die(num)

    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll +1, total))

    print("Average = {}".format(sum(result)/len(result)))
    print("Mean = {}".format(statistics.mean(result)))
    print("Median = {}".format(statistics.median(result)))

    # number_of_rolls = 6000
    # print(random.randint(1,6))


if __name__ == '__main__':
    my_code()
    exit(0)