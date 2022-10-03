#write a program that uses recursion to calculate the nth Fibonacci number

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#function that takes a user input and prints the nth Fibonacci number
def main():
    n = int(input("Enter a number: "))
    print(fib(n))


if __name__ == "__main__":
    main()