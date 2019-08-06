"""
File Info here
"""


def my_code():
    """
    Test function
    :return: 
    """
    s1 = "This is super cool"
    print("Size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)
    # If you need to join large strings, use the join() method instead of + operator
    teams = ["Real Madrid", "barcelona", "Manchester United"]
    record = ":".join(teams)
    print(record)
    print(" ".join(s2))
    print("\n".join(teams))
    print("Split rec", record.split(":"))
    #Partitioning Strings
    departure, separator, arrival = "London:Edinburgh".partition(":")
    departure, _, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)
    t = "London:Edinburgh".partition(":")
    print(t, type(t))
    # String formatting using format
    print("The age of {0} is {1} and the birthday of {0} is {2}".format("Mario", 34, "August 12th"))
    # Omitting the index
    print("The best numbers are {} and {}".format(4,22))


if __name__ == '__main__':
    my_code()
    exit(0)