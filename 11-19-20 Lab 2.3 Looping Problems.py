#Jasmin Salgado
#Lab 2.3
#11/23/20
#CP1


#program 1: print all odd integers from 1 up to the entered value by user
user = int(input("enter a number to print all the odd numbers before it: "))
start = 1

while start <= user:
    print(f'{start}')
    start += 2


#problem 2: print all the Fibonacci #'s up to a certain # of digits
user = int(input("enter the number of digits you want of the Fibonacci sequence: "))
num1 = 0
num2 = 1
count = 0

while count < user:
    print(num1)
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count += 1


#problem 3: sum all integers from 1 to an entered number
num = int(input("enter a number to sum up all the numbers before it starting from 1: "))
start = 0

for(num) in range(num+1):
    start += num
    
print(f'sum of first {num} numbers are: {start}')


#problem 4: computer generates 2 #'s to multiply and user should answer. the program will continue until there was 3 right answers
import random
counter = 0

for i in range(0,3):
    x = random.randint(0,9)
    y = random.randint(0,9)
    print("what is", x, "*", y, "=")
    user = int(input("answer = "))
    if user == x*y:
        print("correct!")
        counter += 1
    else:
        print("incorrect")
        while user != x*y:
            x = random.randint(0,9)
            y = random.randint(0,9)
            answer = x*y
            print("what is", x, "*", y, "=")
            user = int(input("answer = "))
            if user == x*y:
                print("correct!")
                counter += 1
            else:
                print("incorrect")
        
print("congrats you have answered 3 questions right!")


#problem 5: user will input how many numbers, enter the numbers, and will print out which of the numbers is the smallest
list1 = []
user = int(input("how many numbers would you like to enter to determine the smallest number: "))

for i in range(0, user):
    num = int(input("enter numbers: "))
    list1.append(num)
    
print("smallest number is: ", min(list1))


#problem 6: print 5 rows of stars (*)
row = 5
for i in range(1, row+1):
    print('*' * i)


#problem 7: user can input how many rows to print stars (*)
row = int(input("enter a number of rows to print stars: "))

for i in range(1, row+1):
    print('*' * i)


#problem 8: with for loops print the prime numbers from 2-100
n1 = 2
n2 = 100
print("prime numbers between", n1, "and", n2, "are: ")

for num in range(n1, n2 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


#problem 9: user will enter a number of rows, then it will produce a square matrix of alternating x's and o's (checkerboard)
user = int(input("enter a number of rows for the checkerboard: "))
ycounter = 0
xcounter = 0

while ycounter < user:
    while xcounter < user:
        if (ycounter + xcounter) % 2 == 0:
            print("X ", end='')
        else:
            print("O ", end='')
        xcounter += 1
    print()
    ycounter += 1
    xcounter = 0


#problem 10: enter a % to show if it's an A, B, C, D, or F
user = float(input("enter a percentage to see what grade it is: "))

if 89.5 <= user <= 100:
    print("the grade is an A!")
elif 79.5 <= user < 89.5:
    print("the grade is a B")
elif 69.5 <= user < 79.5:
    print("the grade is a C")
elif 59.5 <= user < 69.5:
    print("the grade is a D")
elif user < 59.5:
    print("the grade is an F :/")


#problem 11: same as #10 but repeat until a specific number is entered but make sure the user knows to do that
user = float(input("GUESS the right percentage of the grade: "))
num = 90

while user != num:
    if 89.5 <= user <= 100:
        print("not correct that is an A")
        break
    elif 79.5 <= user < 89.5:
        print("not correct that is a B")
        break
    elif 69.5 <= user < 79.5:
        print("not correct that is a C")
        break
    elif 59.5 <= user < 69.5:
        print("not correct that is a D")
        break
    elif user < 59.5:
        print("not correct that is an F :/")
        break
if user == num:
        print("correct!")

        
#problem 12: calculate the sum of all the digits of a number entered by the user
user = int(input("enter a number to add each digit: "))

addOfNum = sum(int(digit) for digit in str(user))

print(addOfNum)


#problem 13: calculate the average of a set of test scores, it will continue to ask until a -1 is entered then show the average
list1 = []

while True:
    num = int(input("enter the grade of a test score to determine average(enter -1 if done): "))
    if num == -1:
        break
    list1.append(num)
    
print("the average of these test scores are: ", float(sum(list1) / len(list1)), "%")


#problem 14: determine if an entered number is a perfect number
user = int(input("enter a number to determine if it is a perfect number: "))
sum = 0

for i in range(1, user):
    if(user % i == 0):
        sum = sum + i
if (sum == user):
    print("the number", user, "is a perfect number")
else:
    print("the number", user, "is NOT a perfect number")

