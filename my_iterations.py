"""
When working with iterators, generators, etc
Look at the documentation for the itertools module
"""
from itertools import   islice, count, chain
from list_comprehensions import is_prime
# islice "Return an iterator whose next() method returns selected values from an iterable.
#from statistics import average
import statistics

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
    print("List of the prime numbers between 1328 and 1400:",
          list(x for x in range(1328, 1400) if is_prime(x) ))
    print("Are there prime numbers between 1328 and 1362?",
          any(is_prime(x) for x in range(1328, 1362)))

    names = ["London", "New york", "Ogden"]
    print(all(name == name.title() for  name in names ))

    # Another built-in: zip()
    Monday    = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9] # Temp in Celsius
    Tuesday   = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
    Wednesday = [2, 2, 5, 5, 7, 5, 5, 4, 4, 3]

    format_ = ''
    for temps in zip(Monday, Tuesday, Wednesday):
        print("Temperatures in Celsius: max={:6.1f}, min={:6.1f} and  average={:6.1f} ".format( max(temps),
                min(temps), statistics.mean(temps) )) #statistics.mean(temps)

    all_temps = chain(Monday, Tuesday, Wednesday)
    print("All temperature > 0? ", all(t>0 for t in all_temps) )
    print("All temperature > 0? ", all(t>0 for t in temps) )

if __name__ == '__main__':
    my_code()
    exit(0)
