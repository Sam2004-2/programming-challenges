#find the sume of all numbers up to n

#function to find the sum of all numbers up to n
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
        
#call the function
def main():
    n = int(input("Enter a number: "))
    print(sum(n))

if __name__ == "__main__":
    main()
    
        