# Program: Fuctions Lab 2 Methods and Parameters
# Author: Jasmin Salgado
# Last Updated: 2/11/21
# Description: Version 80

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
##    print()

def findMin(scoreArray):
    """find the lowest score"""
    minimum = scoreArray[0]
    for num in scoreArray:
        if num < minimum:
            minimum = num
    return minimum

def findMax(scoreArray):
    """find the highest score"""
    maximum = scoreArray[0]
    for num in scoreArray:
        if num > maximum:
            maximum = num
    return maximum 

def dropLowest(scoreArray):
    """remove the minimum from the list"""
    minimum = findMin(scoreArray)
    scoreArray.remove(minimum)
    return scoreArray

# =========================================================================
# Main Function
def main():
    displayScores(testScores)
##  Remove the comments below to output the 70 pt version
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    print("\nAfter removing the lowest percent")
    testScores2 = dropLowest(testScores)
    newList = displayScores(testScores2)
    
# =========================================================================
# Call the main() function
main()

input("\nPress enter to quit")
