## Lab 1.3 Version 70
## Author: Jasmin Salgado
## Class Period: 1
## Last Modified: 10/8/20


#Calculate the amount of quarters, dimes, nickels, and pennies needed for 97 cents in change
#Output 3 quarters, 2 dimes, 0 nickles, 2 pennies

#start amount of change
cents = 97

#how many quarters can go in
quarters = cents // 25
#how much cents left after quarters
cents = cents % 25

#how many dimes can go in
dimes = cents // 10
#how many cents left after dimes
cents = cents % 10

#how many nickels can go in
nickels = cents // 5
#how many nickels left after dimes
cents = cents % 5

#how many pennies can go in
pennies = cents // 1
#how many cents left after pennies
cents = cents % 1

print(f'Number of coins for 97 cents in change is: ')
print(f'You have {quarters} quarters')
print(f'You have {dimes} dimes')
print(f'You have {nickels} nickels')
print(f'You have {pennies} pennies')

input("Press enter to quit")
