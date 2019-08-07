"""
File Info here
"""


def my_code():
    """
    Test function
    :return:
    """
    for i in range(5):
        print(i)

    # Set the initial value
    print("Now setting initial value")
    for i in range(5,10):
        print(i, type(i))

    # Create a list from range
    l = list(range(5,10))
    print(l, type(l))
    l2 = list(range(5,10)) + list(range(30,40))
    print(l2, type(l2))

    l3=range(10, 20,2 )

    # Iteration over list unsing index notation
    s = [0, 2, 3, 4, 6]
    for i in range(len(s)):
        print(s[i])

    # Better way
    for v in s:
        print(v)

    # enumerate(): returns an iterable series
    t=[6,789, 123, 98, 3,22]
    for p in enumerate(t):
        print(p, p[0], p[1])

    for i, v in enumerate(t):
        print("i = {}, v={}".format(i,v))


if __name__ == '__main__':
    my_code()
    exit(0)