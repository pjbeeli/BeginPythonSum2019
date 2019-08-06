"""
Learn about Python return semantics and how Python functions handles arguments
"""

def egg(var):
    """
    returns the variable back to the user
    :param var: input object
    :return: input object
    """
    return var

# Required parameters must come first
# Optional parameters after required parameters
def banner(message, border_character='*'):
    """
    Print message in banner form
    :param message: String to print
    :param border: border character for string
    :return:
    """
    #length = __len__(message)
    length = message.__len__() +4
    length = len(message) +4
    print_border = border_character*length
    print(print_border)
    print(border_character + " " + message + " " + border_character )
    print(print_border)

def add_spam(menu = None):
    """
    Add spam to the menu list
    :param menu:
    :return: menu list
    """
    if menu is None:
        menu = []

    menu.append('spam')
    return menu


def sum_two(num1, num2=8):
    """
    Sum two input objects
    :param num1: object 1
    :param num2: object 2 (optional), default = 8
    :return: sum of objects
    """
    return num1+num2


def test():
    """
    Test function
    :return:
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)
    n1=3
    n2=9
    print(n1 , " + " , n2, " = ", sum_two(n1, n2))
    print(sum_two("Happy ", "New Year"))
    print(sum_two(n1))
    banner("Weber State University")
    banner("Weber State University","$")

    breakfast = ['eggs', 'bacon']
    print("Before", breakfast)
    add_spam(breakfast)
    print("After", breakfast)

print(__name__)

if __name__ == '__main__':
    test()
    exit(0)

