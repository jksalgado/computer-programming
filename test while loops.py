#how do you find an average?
#add all the scores values and divide by the number of tests


scoreTotal = 0
score= 0
numberOfTests = 0

score = int(input("Enter a test score or -1 to exit: "))

while score != -1:
    scoreTotal += score
    numberOfTests += 1
    score = int(input("Enter a test score or -1 to exit: "))

average = scoreTotal / number OfTests
prit(f'You entered {numberOfTests} with an average of {average}.')
