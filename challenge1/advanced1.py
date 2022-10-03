#find the nth perfect number

#A perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself. Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

#function that takes a user input and prints the nth perfect number
def main():
    n = int(input("Enter a number: "))
    print(perfect(n))

#write a program that uses recursion to calculate the nth perfect number
def perfect(n):
    if n == 0:
        return 0
    elif n == 1:
        return 6
    else:
        return perfect(n-1) + 6*n

if __name__ == "__main__":
    main()