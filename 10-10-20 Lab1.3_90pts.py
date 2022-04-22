## Lab 1.3 Version 90
## Author: Jasmin Salgado
## Class Period: 1
## Last Modified: 10/8/20



#enter coins
quarters = int(input('Enter number of quarters: '))
dimes = int(input('Enter number of dimes: '))
nickels = int(input('Enter number of nickels: '))
pennies = int(input('Enter number of pennies: '))

print(f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies')

value = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1))/100
print(f'Has a total value of: {value}')

input("Press enter to quit")
