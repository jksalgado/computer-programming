# Program: Fuctions Lab 2 Methods and Parameters
# Author: Jasmin Salgado
# Last Updated: 2/10/21
# Description: Version 70

# =========================================================================
# Global Variables
testScores = [90,85,52,74,95,100,78]

# =========================================================================
# Functions

def displayScores(scoreArray):
    """Displays the current test scores"""
    print("The current test scores are:")
    for i in range(len(scoreArray)-1):
        print(float(scoreArray[i]), end= "%, ")
    print(float(scoreArray[len(scoreArray)-1]), end = "%\n")
    print()

def findMin(scoreArray):
    minimum = scoreArray[0]
    for num in scoreArray:
        if num < minimum:
            minimum = num
    return minimum

def findMax(scoreArray):
    maximum = scoreArray[0]
    for num in scoreArray:
        if num > maximum:
            maximum = num
    return maximum 
    
# =========================================================================
# Main Function
def main():
    displayScores(testScores)
##  Remove the comments below to output the 70 pt version
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    
# =========================================================================
# Call the main() function
main()

input("\nPress enter to quit")
