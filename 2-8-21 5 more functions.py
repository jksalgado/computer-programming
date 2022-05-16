#5 more functions
#Jasmin Salgado
#2/8/21

#function 1: greeter w/ default value
def greeter(size = "large"):
    print(f"hello! would you like a {size} order of fries with your order?")

greeter()

#function 2: when it's the weekend and output a boolean value
def weekend(day):
    if day.lower() == "saturday" or day.lower() == "sunday":
        return True
    else:
        return False

day1 = weekend("Saturday")
print(day1)

#function 3: surface area for paint
def area(height, width):
    surfaceArea = height*width
    return surfaceArea

total = area(10, 12)
if total <= 63:
    print("you need about 1 gallon of paint")
else:
    amount = total/63
    print(f"you need {amount} gallons of paint")

#function 4: cost calculator for paint
def cost(costOfGallon, gallons):
    totalCost = costOfGallon*gallons
    return totalCost

total = cost(20, 5)
print(total)

#function 5: surface cost calculator for paint (funtion 3 + function 4)
def cost(height, width, costOfGallon):
    surfaceArea = ((height*width)/63)*costOfGallon
    return surfaceArea

total = cost(10, 10, 20)
print(total)

input("press enter to quit")
