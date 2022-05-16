###take in a string
##text = input("enter your phrase: ")
##newText = ''
##vowel = 'aeiou'
##
###output that same string without vowels
##for letters in text:  #goes through each character of the input text
##    if letters.lower() not in vowel:   #checks if character is in vowels
##        newText += letters   #if character isn't a vowel adds it to new string
##
##print(f'your new message \n{newText}')
##input('press enter to exit')


#problem 1:
#create a program that will count the number of words that are in a short phrase
#or sentence
#(what single character can you search for to help find the # of words that
#exist)

text = input('enter phrase: ')
word = ' '
count = 1

for characters in text:
    if characters in word:
        count += 1

print(f'there are {count} words')


#problem 2:
#allow the user to input a single letter and have the program search for that
#letter in a string
#it should print out the the indices of where that letter is found
#if word is banana
#we want location of a
#1 3 5
text = input("enter phrase: ")
letter = input("what letter to look for: ")
for i in range(len(text)):
    if text[i] == letter:
        print(i, end = ' ')

#problem 3:
#allow the user to enter a single letter and allow the program to fill in
#that letter in each position that letter exist from a given string.
#otherwise it should fill in underscores to represent another letter in that
#spot. like a game of hangman.
word = "python"
guess = input("guess a letter: ")
for characters in word:
    if characters == guess:
        print(guess, end = ' ')
    else:
        print("_", end = ' ')

        
    
