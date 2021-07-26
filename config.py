import pygame
import random

pygame.init()

FPS = 60
scrn_wid = 750
scrn_heig = 750
stage = "main_menu"
organism_type = "bacteria"
bacteria_desc = "Bacteria are microscopic decomposers."
fungus_desc = "Fungi are plant fertilizers. "
upgradeoptions = ["Master (No More Upgrades)","Tail I (Walk Speed: + 5)","Tail I (Walk Speed: + 5)","Tail II (Walk Speed: + 10)","Tail II (Walk Speed: + 10)","Tail III (Walk Speed: + 20)"]
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

RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (102, 0, 204)
BROWN = (139,69,19)

def show_text(msg, x, y, color, size, screen):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

def touching(obj1x,obj1y,obj2x,obj2y,obj2length, obj2width):
    if obj1x in range(obj2x, obj2x + obj2length - 1) and obj1y in range(obj2y, obj2y + obj2length - 1):
        return True
    if obj1x in range(obj2x, obj2x + obj2width - 1) and obj1y in range(obj2y, obj2y + obj2width + 1):
        return True
    else:
        return False

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
