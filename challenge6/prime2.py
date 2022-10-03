#Write a function which can find all the primes in an array, and return an array with said primes!

import numpy as np 


def main():
    n = np.arange(150)
    print(n)
    print(n[is_prime_array(n)]) 


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5 + 1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime_array(n):
    return np.array([is_prime(x) for x in n]) 


if __name__ == "__main__":
    main()



