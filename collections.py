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

def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def my_code():
    """
    Test function
    :return: 
    """
    do_tuples()


if __name__ == '__main__':
    my_code()
    exit(0)