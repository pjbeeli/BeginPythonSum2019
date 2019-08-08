"""
When working with iterators, generators, etc
Look at the documentation for the itertools module
"""
from itertools import   islice, count
from list_comprehensions import is_prime
# islice "Return an iterator whose next() method returns selected values from an iterable.

def my_code():
    """
    Test function
    :return: 
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000) # this is not computationally performed here
    print(thousand_primes, type(thousand_primes)) # doesn't execute

    print("List of first 1K prime numbers:", list(thousand_primes))

    # Need to re-generate object
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first 1K prime numbers:", sum(thousand_primes))

    # other built-in for use with itertools: any, all
    print(any([False, False, True])) # OR gate
    print(all([False, False, True])) # AND gate

    # print(list(islice(x for x in range(1328, 1362) if is_prime(x))), )
    print("Are there prime numbers between 1328 and 1362?",
          any(is_prime(x) for x in range(1328, 1362)))

if __name__ == '__main__':
    my_code()
    exit(0)
