"""
Learn about sets
An unordered collection of unique, immutable objects
Define it using {}  (just like a dictionary, but we don't need a key)
"""


def my_code():
    """
    Test function
    :return: 
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1,3,4,2, 88, 3, 1]
    print(data, type(data))
    # eliminate duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    # Iterate with for
    for item in sdata:
        print(item)

    # Supports membership testing: in, not in
    print(5 in sdata)
    # Adding elements to sets:
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])
    print(sdata)

if __name__ == '__main__':
    my_code()
    exit(0)