"""
Learn about iterable, iterator objects
Use the built-in
 iter(): create an iterable object
 next(): fetch the next element in the iterable object
"""

def first(iterable):
    """
    Return the next member of the list IF available
    :param iterable: iterable object
    :return: Next member or
    :except: Value Error for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

def my_code():
    """
    Test function
    :return: 
    """
    iterable = ["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable) # give me an iterator
    print(type(iterator), iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    print("*",first(iterable))
    print("*",first(iterable))

if __name__ == '__main__':
    my_code()
    exit(0)