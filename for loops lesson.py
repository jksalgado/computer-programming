#display the number from 0-10
for numbers in range(0,11):
    print(numbers)

#display the number from 10-20
for numbers in range(10,21):
    print(numbers, end = ' ')

#display numbers from 20 to 1
for i in range(20,0,-1):
    print(i, end = ' ')

#display multiples of 5 from 0-100
for factors in range(0,101,5):
    print(factors, end = ' ')

#count the characters of a short phrase entered by the user
phrase = input("tell me something: ")
counter = 0
for characters in phrase:
    counter += 1
    
print(counter)
