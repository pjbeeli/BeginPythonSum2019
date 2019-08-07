"""
Learn about list()
"""


def my_code():
    """
    Test function
    :return: 
    """
    s = "show how to do it".split()
    print(s, type(s))
    print("s[3]", s[3])

    print("last member", s[len(s)-1]) # C style
    print("last member", s[-1]) # more pythonic (negative indices)
    # Slicing
    print("From 1 to one before the last member", s[1:-1])
    print("From 1 to three members",s[1:3])
    print("From 1 to end", s[1:])
    print("From beginning to end", s[:])

    # Make a copy of list
    t = s # shallow copy (share pointer)
    print("s:",s)
    print("t:",t)
    t = print("t is s", t is s)
    print("t==s:", t==s)

    # Make a copy of list
    t = s[:] # deep copy
    # or this: t = s.copy()
    # or this: t = list(s)
    print("s:",s)
    print("t:",t)
    t = print("t is s", t is s)
    print("t==s:", t==s)

    # Shallow copies
    # A list of list
    a =[[1,2], [3,4]]
    print(a,type(a))
    print("a[0]:",a[0])
    print("a[0][1]:",a[0][1])

    # Copy the list of list
    b = a[:]
    a[0]=[-3,-2]
    print('a==b:', a == b)

if __name__ == '__main__':
    my_code()
    exit(0)