import pygame
import random

pygame.init()

organism_type = "bacteria"
bacteria_desc = "Bacteria are microscopic decomposers."
fungus_desc = "Fungi are plant fertilizers. "
upgradeoptions = ["Master (No More Upgrades)","Tail I (Walk Speed: + 5)","Tail II (Walk Speed: + 10)","Tail III (Walk Speed: + 20)"]
upgrades = []
upgrade = "NONE"
playerx = 340
playery = 285
right = False
left = False
up = False
down = False
upgradeable = True
walkspeed = 5
foodval = 0
foodgoal = 10
food_spots = []

def genmap():
    for i in range(1, 11, 1):
        chance = random.randint(0, 100)
        chance = random.randint(0, 2)
        foodval = "NONE"
        if chance == 1:
            trueorfalse = "True"
        else:
            trueorfalse = "False"
        food_spots.append(((random.randint(0, 720), random.randint(0,580)), trueorfalse))

#genmap()
