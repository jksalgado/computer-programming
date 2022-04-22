## Lab 1.3 Conversion Lab Version 110
## Author: Jasmin Salgado
## Class Period: 1
## Last Modified: 10/9/20


import random

quarters = random.randint(50,100)
print('Total Quarters: ' + str(quarters))

dimes = random.randrange(50,101)
print('Total Dimes: ' + str(dimes))

nickels = random.randint(50,100)
print('Total Nickels: ' + str(nickels))

pennies = random.randrange(50,101)
print('Total Pennies: ' + str(pennies))

print()
value = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1))/100
print(f'total value of all the coins is: ${value}')
print()

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
print(f'Ones: {Ones}')
print(f'Quarters: {Quarters}')            
print(f'Dimes: {Dimes}')
print(f'Nickels: {Nickels}')
print(f'Pennies: {Pennies}')
print()

input("Press enter to quit")
