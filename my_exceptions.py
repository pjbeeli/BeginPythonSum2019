"""
Learn about exceptions
"""
import sys

def convert(s):
    """
    Converts a string to integer
    :param s:
    :return:
    """
    # x = -1
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error {}".format(str(e)), file=sys.stderr) #, file=sys.stderr

    return -1

def sqrt(x):
    """
    Compute the sqrt using the method of Heron of Alexander
    :param x:  number to copute the sqrt
    :return:  the sqrt of x
    """
    guess = x
    i = 0
    print(x, end=' ')
    while guess * guess != x and i <20:
        guess = (guess +x/guess)/2.0
        i += 1
        print(i,',', guess, end='; ')
    return guess

def my_code():
    """
    Test function
    :return: 
    """
    print(convert("22"))

    # print(convert("-1"))
    # print(convert([1,4,8]))
    try:
        print(convert("Hello"))
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-3))
    except ValueError:
        print("Cannot compute the value of negative numbers")

    print("Done")

if __name__ == '__main__':
    my_code()
    exit(0)