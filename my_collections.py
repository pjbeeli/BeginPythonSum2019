"""
Learn about collections: Tuples, Strings, Range, List
"""


def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    # Use () to define a tuple (tuple is a heterogeneous immutable sequence)
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size", len(t))
    print("One member:", t[0])
    # To iterate over a tuple
    for item in t:
        print(item)

    #Single tuples, must end with comma
    t1 = (6,) # weird eh?
    print(t1, type(t1))
    # Another way to create tuples parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))
    # Tuple unpacking
    lower, upper = min_max([56, 76, 11, 12, 90])
    print("min", lower)
    print("max", upper)
    a = "jelly"
    b = "bean"
    print(a,b)
    # Call your function
    a,b = swap(a,b)
    print(a,b)

    t2 = 1, 2, 3, 5
    print(t2, type(t2))
   # Tuple constructor: tuple()
    t_from_l = tuple([3, 77, 11])
    print(t_from_l, type(t_from_l))
   # test for membership)
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))

def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def swap(a,b):
    """
    Swamp the values of a and b
    :param a:
    :param b:
    :return:
    """
    return b, a


def my_code():
    """
    Test function
    :return: 
    """
    do_tuples()
    # print(min_max([56, 76, 11, 12, 90]))
    # output = min_max([56, 76, 11, 12, 90])
    # print("min", output[0])
    # print("max", output[1])



if __name__ == '__main__':
    my_code()
    exit(0)