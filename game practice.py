from random import*

hero = []

loot_drop = ["gold", "rock", "bones", "chicken leg", "weapons"]

print('congrats you defeated the bad buy')
item = loot_drop[randrange(len(loot_drop))]

print(f'you have picked up {item}')
hero.append(item)
print(f'your new inventory is {hero}
