# Program: Fuctions Lab 2 Methods and Parameters
# Author: Jasmin Salgado
# Last Updated: 2/13/21
# Description: Version 110

# =========================================================================
# Global Variables
testScores = []
while True:
    num = int(input("Test score: (enter -1 if done): "))
    if num == -1:
        break
    testScores.append(num)
    
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
    """find the lowest test score"""
    minimum = scoreArray[0]
    for num in scoreArray:
        if num < minimum:
            minimum = num
    return minimum

def findMax(scoreArray):
    """find the highest test score"""
    maximum = scoreArray[0]
    for num in scoreArray:
        if num > maximum:
            maximum = num
    return maximum 

def dropLowest(scoreArray):
    """remove the minimum from the test scores"""
    minimum = findMin(scoreArray)
    scoreArray.remove(minimum)
    return scoreArray

def getMean(scoreArray):
    """find average/mean of the test scores"""
    num = 0
    mean = 0
    for i in scoreArray:
        num += 1
        mean += i
    mean /= num
    return mean

def getMedian(scoreArray):
    """find the median of the test scores"""
    scoreArray.sort()
    if len(scoreArray) % 2 == 2:
        return scoreArray[len(scoreArray)//2]
    else:
        return (scoreArray[len(scoreArray)//2-1] + scoreArray[len(scoreArray)//2]) / 2
    
# =========================================================================
# Main Function
def main():
    displayScores(testScores)
##  Remove the comments below to output the 70 pt version
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    print("\nAfter removing the lowest score")
    testScores2 = dropLowest(testScores)
    newList = displayScores(testScores2)
    mean = getMean(testScores)
    print("Average: ", mean)
    median = getMedian(testScores)
    print("Median: ", median)
    
# =========================================================================
# Call the main() function
main()

input("\nPress enter to quit")
