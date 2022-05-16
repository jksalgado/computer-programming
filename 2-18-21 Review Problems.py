# Review Problems for Functions
# Jasmin Salgado
# 2/17/21
# CP1


# 1: hypotenuse calculation
# function name: hypothenuse  with 2 parameters: the sides of the right triangle
def hypotenuse(leg1, leg2):
    # calculate the hypotenuse of a right triangle
    leg3 = (leg1)**2 + (leg2)**2
    leg3 = (leg3)**(1/2)
    # return hypotenuse
    return leg3

hypotenuse = hypotenuse(3, 4)
print("the hypotenuse is ", hypotenuse)


# 2: multiples
# function name: isMultiple  with 2 parameters: pair of integers
def isMultiple(integer1, integer2):
    # determine if the second integer is a multiple of the first
    if integer2 % integer1 == 0:
        # return True or False based on description
        return True
    else:
        return False

integers = isMultiple(4,20)
print(integers)


# 3: perfect numbers
# function name: isPerfect  with 1 parameter: an integer
def isPerfect(integer):
    for i in range(1, integer):
        # return True if it is a perfect number
        if integer % i == 0:
            return True
        # return False if it's not
        else:
            return False

number = isPerfect(28)
print(number)


# 4: right triangle
# function name: isRight  with 3 parameters: sides of a triangle
def isRight(x, y, hypotenuse):
    # return True if the values are sides of a right triangle
    if (x**2 + y**2) == hypotenuse**2:
        return True
    # return false if not a right triangle
    else:
        return False

triangle = isRight(6, 8, 10)
print(triangle)


# 5: distance between points
# function name: findDistance  with 4 parameters: x and y of each point
def findDistance(x1, y1, x2, y2):
    # return the distance between the 2 points
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return distance

distanceForPoints = findDistance(3, 9, 6, 13)
print(distanceForPoints)



input("\npress enter to exit")
