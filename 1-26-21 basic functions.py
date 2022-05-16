##Jasmin Salgado
##Simple functions
##1/27/21


# greeter
def greeting():
    print("hello")


greeting()


# need to go to school based on day
def school(day):
    if day.lower == "saturday" or day.lower == "sunday":
        print("go back to bed you don't have school")
    else:
        print("you have school :/")

school("sunday")

# volume of cylinder
def volume(radius, height):
    v = 3.14159 * (radius ** 2) * (height)
    return v


cylinder = volume(5, 10)
print(cylinder)


# volume of rectangular prism
def volume(length, width, height):
    v = length * width * height
    return v


rectPrism = volume(10, 6, 9)
print(rectPrism)


# function i want to do, just multiplying two numbers
def multiply(x1, x2):
    m = x1 * x2
    return m


multiplication = multiply(23, 46)
print(multiplication)
