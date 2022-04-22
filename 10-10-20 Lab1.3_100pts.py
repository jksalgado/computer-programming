## Lab 1.3 Version 100
## Author: Jasmin Salgado
## Class Period: 1
## Last Modified: 10/8/20



#enter coins
quarters = int(input('Enter number of quarters: '))
dimes = int(input('Enter number of dimes: '))
nickels = int(input('Enter number of nickels: '))
pennies = int(input('Enter number of pennies: '))

value = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1))/100
print(f'toatl value of all the coins is: ${value}')

Twenties = int(value // 20)
value = value % 20

Tens = int(value // 10)
value = value % 10

Fives = int(value //5)
value = value % 5

Ones = int(value // 1)
value = value % 1

Quarters = int(value // .25)
value = value % .25

Dimes = int(value // .10)
value = value % .10

Nickels = int(value // .05)
value = value % .05

Pennies = int(value // .01)
value = value % .01

print(f'Twenties: {Twenties}')
print(f'Tens: {Tens}')
print(f'Fives: {Fives}')
print(f'One: {Ones}')
print(f'Quarters: {Quarters}')            
print(f'Dimes: {Dimes}')
print(f'Nickels: {Nickels}')
print(f'Pennies: {Pennies}')

input("Press enter to quit")
