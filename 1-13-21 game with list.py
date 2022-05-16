#text based adventure

from random import*
#name a character
name = input("what will your character be called? ")
print(f'all hail the mighty chimpunk {name}')


#give character health/str stats
stats = [100, 20]  #health, strength


#give character inventory
inventory = [10, 'reality stone']  #first item is money (nuts)


#while alive fight monster
while stats[0] > 0:   #while your health is greater than 0
    print('you have encountered a Hoomaon, prepare to fight')
    enemyValue = randint(0,5)
    playerHit = randint(0,stats[1])
    if enemyValue >= playerHit:
        print(f'you have been defeated and loose {enemyValue} health')
        stats[0] -= enemyValue
        print(f'you now have {stats[0]} health')
        input()
    else:
        print('you have slained the Hoomaon')
        print('you have earned {playerHit-enemyValue} nuts')
        inventory[0] += (playerHit-enemyValue)
        print(inventory)
    shop = input('do you want to go shopping yes/no? ")
    if shop.lower() = 'yes':
    
#win loot


#take over world and universe
