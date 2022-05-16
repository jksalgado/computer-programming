##Selection Problems
##Jasmin Salgado
##CP1
##11/7/20


##Problem 1: from age see if user is eligible or not to vote
user = int(input("Enter your age: "))

if user >= 18:
    print("You are eligible to vote for the upcoming election!")
else:
    print("You are too young to vote in the election :(")


##Problem 2: from percentage entered by user display what letter grade it is
user = float(input("Enter a percentage to see what grade it is: "))

if 89.5 <= user <= 100:
    print("The grade is an A!")
elif 79.5 <= user < 89.5:
    print("The grade is a B")
elif 69.5 <= user < 79.5:
    print("The grade is a C")
elif 59.5 <= user < 69.5:
    print("The grade is a D")
elif user < 59.5:
    print("The grade is an F :/")


##Problem 3: randomly generate 2 single digit numbers to multiply so the user can enter the answer
import random
x = random.randint(0,9)
y = random.randint(0,9)

print("What is", x, "*", y, "=")
user = int(input("Answer = "))

if user == x*y:
    print("Correct!")
else:
    print("Incorrect")


##Problem 4: determine if 3 sides of a triangle for a right triangle
leg1 = int(input("Enter the length of the first leg: "))
leg2 = int(input("Enter the length of the second leg: "))
hyp = int(input("Enter the length of the hypotenuse: "))

if ((leg1)**2) + ((leg2)**2) == ((hyp)**2):
    print("These lengths form a right triangle")
else:
    print("These lengths do not form a right triangle")

