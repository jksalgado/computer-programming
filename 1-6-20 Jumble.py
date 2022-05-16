#game of jumble
from random import*

#select the word to be guessed
word_bank = ['chicken', 'steak', 'pork', 'avocado', 'salsa', 'cheese', 'peppers', 'onions', 'lettuce', 'beans', 'tortilla']
word_bank_length = len(word_bank)
random_index = randrange(0,word_bank_length)
random_word = word_bank[random_index]
original_word = random_word

#scramble the word
#loop through the word, as i pick a letter cross/cancel it out?
scrambled_word = ''
while random_word != '':
    i = randrange(0,len(random_word))
    scrambled_word += random_word[i]
    random_word = random_word[:i]+random_word[i+1:]

print(scrambled_word)

#enter guesses for word
guess = input('try to guess the word: ')
while guess != original_word:
    print('try again')
    print(scramble_word)
    guess = input('try to guess the word: ')

print(f'you are correct. the word was {original_word}')
