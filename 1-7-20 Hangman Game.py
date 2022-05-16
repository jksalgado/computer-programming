#Lab 5.2 Hangman
#Jasmin Salgado
#CP1
#1/7/20

from random import*
print("WELCOME TO THE GAME OF HANGMAN")


# Hangman Tuple to use for hangman art
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

#last index of hangman tuple
max_wrong = 7
guessed_word = ''
missed_letters = []

###variables we need
#work bank
word_bank = ["computer","apple","backpack","pancakes","water","sleep"]
#selected word
word_bank_length = len(word_bank)
random_index = randrange(0,word_bank_length)
random_word = word_bank[random_index]
random_word_length = len(random_word)
original_word = random_word

#blank answer
for i in range(random_word_length):
    guessed_word += "_ "

scrambled_word = ''
while random_word != '':
    i = randrange(0,len(random_word))
    scrambled_word += random_word[i]
    random_word = random_word[:i]+random_word[i+1:]

###operation
#input letter
while "_ " in guessed_word and max_wrong >0:
    print(guessed_word)
    print(scrambled_word)
    print(f'missed letters {missed_letters}')
    letter = input("guess a letter in the word: ")

#check if letter is in word
if letter in random_word:
    location = random_word.find(letter)
    guessed_word = guessed_word[:location]+letter+guessed_word[(location+1)]
else:
    max_wrog -= 1
    print(f'you have {max_wrong} lives remaining')
    missed_letters.append(letter)
print(guessed_word)



#repeat until word is guessed or not of trys


#index starts at 0
