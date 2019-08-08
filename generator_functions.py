"""
Learn about generator functions:
- Describe iterables series with code functions
- Are lazy evaluated: the next value in the sequence is computed on demand
_ Can model infinite series/sequences: data streams, mathematical series with no end
- Can use pipelines

use the yield keyword
"""

def gen123():
    yield 1
    yield 2
    yield 3

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yeild 4")
    yield 4
    print("About to yeild 6")
    yield 6

def my_code():
    """
    Test function
    :return:
    """
    g=gen123()
    print(g, type(g))
    # yield next value
    print(next(g))
    # iterate over the generator function
    for v in gen123():  # kind of like a for loop over a function
        print(v)

    h = gen246()
    print(next(h))
    print(next(h))
    print(next(h))
    # print(next(h))

if __name__ == '__main__':
    my_code()
    exit(0)
