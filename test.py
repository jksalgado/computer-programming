import random

def ask_number(question, low, high):
    """ask a number within range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
        return response

answer = random.randrange(1,10)
guess = None

print(answer)
##while guess != answer:
ask_number("\nplease pick a number between 1 and 10\t",1,10)

print("congrats")
