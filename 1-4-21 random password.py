from random import*

#program will generate a randon password of givin length
password = ''

#enter how many letters are desired
llength = int(input("how many lower letters should the password have?"))
ulength = int(input("how many upper letters should the password have?"))
numbers = int(input("how many numbers should the password have?"))

#select letters
lalphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(llength):
    pick = lalphabet[randint(0,len(lalphabet)-1)]
    password += pick

ualphabet = 'QWERTYIOPASDFGHJKLZXCVBNM'
for i in range(ulength):
    pick = ualphabet[randint(0,len(ualphabet)-1)]
    password += pick

numberList = '0123456789'
for i in range(numbers):
    pick = numbers[randint(0,len(numberList)-1)]
    password += pick
print(password)

#scramble letters
newPassword = ''
while len(password)>0:
    pick = password[randint(0,len(password))]
    password = password[:plae
