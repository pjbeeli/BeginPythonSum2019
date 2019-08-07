"""
List Comprehensions
Readable, expressive and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp

def is_prime(n):
    """
    Determine whether a number is bring
    :param n: number to be tested
    :return: boolean (TRUE or FALSE)
    """
    # if n%2 == 0 or

    if n<2:
        return False
    for i in range(2, int(sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def my_code():
    """
    Test function
    :return: 
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    data = [] # empty list
    for word in words:
        # Some analysis ...
        data.append(word)
    # "Filter" data
    print(data)

    # Task: Find the length of the first 20 factorial numbers
    count = []
    for x in range(20):
        fa = factorial(x)
        cnt= len(str(fa))
        print(fa, ' ', len(str(fa)))
        count.append(len(str(fa)))
    print(count, type(count))

    # Use a comprehension
    info2 = [len(str(factorial(x))) for x in range(20) ]
    print(info2, type(info2))

    # Set Comprehensions: {}
    info3 = {len(str(factorial(x))) for x in range(20) }
    print(info3, type(info3))

    # Dictionary Comprehensions
    nba_teams = {'jazz':'SLC', 'Warriors':'oakland', 'lakers':'LA', 'clippers':'LA'}
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    primes = [x for x in range(1001) if is_prime(x)] # the "if is_prime(x)" is a filter
    print(len(primes),primes)

if __name__ == '__main__':
    my_code()
    exit(0)