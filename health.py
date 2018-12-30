# Health Potion Game using python version 3.7.2

#The player has a variable health, depending of the difficulty option easy, medium and advanced the potion health will change.
#Health potion will have a random number when selected by player

import random

health = 50
print("The health of the player is", + health)

difficulty = random.randrange(1,3)
print("The difficulty of the player is (1 = easy, 2 = medium, 3 = advanced", + difficulty)

potion_health= int(random.randint(25,50)/difficulty)
print("The potion health of the player is", + potion_health)

#Player will have whatever health has and add random potion health
health = health + potion_health

print("The total health of the player which is the sum health plus potion health is", + health)
