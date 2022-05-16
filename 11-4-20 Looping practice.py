#Looping Problems
#Jasmin Salgado
#CP1
#11/2/20


#problem 1: print all the even numbers from 2 to entered number by user.
x = int(input("Enter number: "))
start = 2
while start <= x:
    print(f'{start}')
    start += 2

 
#problem 2: sum all the integers from 1 up to value entered by user.
x = int(input("Enter number: "))
start = 0
for(num) in range(x+1):
    start += num

print(f'sum of first {x} number is: {start}')


#problem 3: calculate the factoral of a number.
x = int(input("Enter number: "))
n = x
fact = 1
while(n >= 2):
    fact = fact*n
    n -= 1

print(f'{x} factorial is equal to: {fact}')


#problem 4: diplay a triangle of stars equal to the row the user is in.
row = int(input("Enter row number: "))
for i in range(1, row+1):
    print('*' * i)

input("Press enter to quit")
