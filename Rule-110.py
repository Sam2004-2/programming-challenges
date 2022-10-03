#  This python function calculates the next iteration of Rule 110
#  The function considers indexes outside the bounds of the list to be 0
#  The function returns a list of 0s and 1s

def rule110(iteration):
    #  Create a list of 0s the same length as the input list
    next_iteration = [0] * len(iteration)
    #  Loop through the input list
    for i in range(len(iteration)):
        #  Calculate the next value by looking at the current value and the two values to the left and right
        next_iteration[i] = (iteration[i-1] + iteration[i] + iteration[(i+1) % len(iteration)]) % 2
    return next_iteration

def main():
    #  Create a list of 0s
    iteration = [0]
    #  Loop 100 times
    for i in range(100):
        #  Print the list
        print(iteration)
        #  Calculate the next iteration
        iteration = rule110(iteration)
    
        
if __name__ == "__main__":
    main()
    
# This is a shoddy job at a rule 110 generator. Much needed to improve. Could have possibly used graphics library to display the output in a more visual way.

