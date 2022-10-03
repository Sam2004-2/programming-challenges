# PROGRAMMING CHALLENGE 3
 
 
#  	Write a parser which takes a given set of instructions and prints an output based on the instructions.
 
#  	parser begins with a value at zero
#  	'i' = increments the value
#  	'd' = decrements the value
#  	's' = squares the value
#  	'o' = outputs the value and resets it to zero
 	
#  	Instructions are stored as strings and passed into the parser
 
#  	EXAMPLE CASES: "iio": 2
#  				   "iiisso": 81
#  				   "iido": 1
#  				   "iisoiiso": 4 4

import sys

instructions = input("Enter instructions: ")

#function to parse the instructions
def parser (instructions):
    #initialize the value
    value = 0
    #loop through the instructions
    for i in range(len(instructions)):
        #increment the value
        if instructions[i] == 'i':
            value += 1
        #decrement the value
        elif instructions[i] == 'd':
            value -= 1
        #square the value
        elif instructions[i] == 's':
            value = value**2
        #output the value
        elif instructions[i] == 'o':
            print(value)
            value = 0
        #if the instruction is not valid, print an error
        else:
            print("Error: Invalid instruction")
            sys.exit()
    #if there is a value left over, print it
    if value != 0:
        print(value)
    return

#call the function
def main():
    parser(instructions)
    
if __name__ == "__main__":
    main()



 