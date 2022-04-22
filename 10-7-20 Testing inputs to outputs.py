#user enters in how old they are in years
#outputs number of days old


ageYears = int(input('How old are you: '))
ageDays = ageYears*365
print(f"You are {ageDays} days old")

input('press enter to quit')


quarters = int(input("How many quarters do you have?:" ))
dimes = int(input('How many dimes do you have?:' ))
nickels = int(input("How many nickels do you have?:" ))
pennies = int(input('How many pennies do you have?:' ))
totalCents = (quarters*25)+(dimes*10)+(nickels*5)+(pennies*1)
totalDollars = totalCents/100
print(f'Your total value of money is ${totalDollars}')


#user to input how tall they are in inches
#output the users height (x ft y in)
# i.e. input =20 output = 1 ft 8 in

tallInches = int(input('How tall in iches are you?:' ))
height = tallInches/12
