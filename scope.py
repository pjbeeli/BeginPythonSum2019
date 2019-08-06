"""
Learn about scoping in Python
L - local
E - enclosing
G - global
B - built in
"""
count = 0 # global object

def show_count():
    """
    Display the current count
    :return: nothing
    """
    print(count)

# def set_count(count, num = 0):
#     """
#     set the count
#     :param num: num
#     :return: count
#     """
#     count = num
#     return count

def set_count(num = 0):
    """
    set the count
    :param num: num
    :return: nothing
    """
    global count
    count = num



def main():
    """
    Test function
    :return: 
    """
    show_count()
    set_count(9)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)