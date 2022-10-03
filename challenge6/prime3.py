#Write a function which can find all the twin prime pairs in an array, make each pair into an array, and then finally add them pairs to their own array!

import numpy as np

def main():
    n = np.arange(1000)
    
    print(n)
    
    print(n[is_prime_array(n)]) 
    
    print(twin_prime_array(n))

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

def twin_prime_array(n):
    return np.array([[x,x+2] for x in n if is_prime(x) and is_prime(x+2)])


if __name__ == "__main__":
    main()
