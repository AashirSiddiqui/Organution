from pygame.locals import *
import pygame
import random
import time

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


screen = pygame.display.set_mode((scrn_wid, scrn_heig))
clock = pygame.time.Clock()
pygame.display.set_caption("Organution")

bacteria = pygame.image.load("bacteria.png")
bacteria = pygame.transform.scale(bacteria, (50, 100)).convert()

fungus = pygame.image.load("fungus.png")
fungus = pygame.transform.scale(fungus, (50, 100)).convert()

food_uneaten = pygame.image.load("food1.png").convert()
food_uneaten = pygame.transform.scale(food_uneaten, (40, 40))

food_eaten = pygame.image.load("food2.png").convert()
food_eaten = pygame.transform.scale(food_eaten, (40, 40))

background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (720, 720))

deathframe = pygame.image.load("deathframe.png").convert()
deathframe = pygame.transform.scale(deathframe, (750, 750))

while True:
    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        print(food_spots)
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            if stage == "main_menu":
                stage = "create_organism"
            elif stage == "create_organism":
                if touching(mousepos[0], mousepos[1], 40, 175, 200, 100) == True:
                    # bacteria button
                    organism_type = "bacteria"
                if touching(mousepos[0], mousepos[1], 260, 175, 200, 100) == True:
                    # fungus button
                    organism_type = "fungus"
                if touching(mousepos[0], mousepos[1], 480, 175, 200, 100) == True:
                    # play button
                    genmap()
                    stage = "main_game"
            elif stage == "game_over":
                stage = "create_organism"
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                right = True
                left = False
                down = False
                up = False
            elif event.key == K_LEFT:
                left = True
                right = False
                down = False
                up = False
            elif event.key == K_UP:
                up = True
                down = False
                left = False
                right = False
            elif event.key == K_DOWN:
                down = True
                up = False
                left = False
                right = False
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                right = False
            elif event.key == K_LEFT:
                left = False
            elif event.key == K_UP:
                up = False
            elif event.key == K_DOWN:
                down = False
    if stage == "main_menu":
        show_text("Organution", 160, 125, BLUE, 100, screen)
        show_text("Click Anywhere To Start", 265, 250, WHITE, 25, screen)
    elif stage == "create_organism":
        show_text("Create Organism", 60, 25, WHITE, 100, screen)
        BacteriaButton = pygame.draw.rect(screen, BLUE, (40, 175, 200, 100), 0)
        show_text("Bacteria", 65, 195, BLACK, 50, screen)
        FungusButton = pygame.draw.rect(screen, RED, (260, 175, 200, 100), 0)
        show_text("Fungus", 290, 195, BLACK, 50, screen)
        PlayButton = pygame.draw.rect(screen, GREEN, (480, 175, 200, 100), 0)
        show_text("PLAY", 510, 185, BLACK, 70, screen)
        if organism_type == "bacteria":
            show_text(bacteria_desc, 10, 720, WHITE, 20, screen)
            screen.blit(bacteria, (335, 400))
        elif organism_type == "fungus":
            show_text(fungus_desc, 10, 720, WHITE, 20, screen)
            screen.blit(fungus, (335, 400))
    elif stage == "main_game":
        screen.blit(deathframe, (0, 0))
        screen.blit(background, (15, 15))
        show_text("FOOD: "+str(foodval), 10, 700, BLACK, 25, screen)
        show_text("WALKSPEED: "+str(walkspeed), 10, 650, BLACK, 25, screen)
        show_text("LAST UPGRADE: "+str(upgrade), 10, 600, BLACK, 25, screen)
        if right == True:
            if playerx + 50 < 750:
                playerx = playerx + walkspeed
            else:
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
                food_spots=[]
                stage = "game_over"
        elif left == True:
            if playerx > 0:
                playerx = playerx - walkspeed
            else:
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
                food_spots=[]
                stage = "game_over"
        elif up == True:
            if playery > 0:
                playery = playery - walkspeed
            else:
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
                food_spots=[]
                stage = "game_over"
        elif down == True:
            if playery + 100 < 750:
                playery = playery + walkspeed
            else:
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
                food_spots=[]
                stage = "game_over"
        if organism_type == "bacteria":
            screen.blit(bacteria, (playerx, playery))
        elif organism_type == "fungus":
            screen.blit(fungus, (playerx, playery))
        v = 0
        if foodval == foodgoal and upgradeable == True:
            upgrade = random.choice(upgradeoptions)
            upgrades.append(upgrade)
            print(upgrade)
            if "Tail I" in upgrade:
                walkspeed = walkspeed + 5
            elif "Tail II" in upgrade:
                walkspeed = walkspeed + 10
            elif "Tail III" in upgrade:
                walkspeed = walkspeed + 20
            elif "Master" in upgrade:
                upgradeable = False
            foodval = 0
        for spot in food_spots:
            if spot == (spot[0], "True"):
                screen.blit(food_uneaten, (spot[0][0], spot[0][1]))
                if touching(spot[0][0], spot[0][1], playerx, playery, 50, 100) == True:
                    food1 = (spot[0], "False")
                    foodval = foodval + 1
                    food_spots.pop(v)
                    food_spots.insert(v, food1)
            if spot == (spot[0], "False"):
                screen.blit(food_eaten, (spot[0][0], spot[0][1]))
                if random.randint(1, 1000) == 2:
                    spot1 = (spot[0], "True")
                    food_spots.pop(v)
                    food_spots.insert(v, spot1)
            v = v + 1
    elif stage == "game_over":
        show_text("Game Over", 160, 125, RED, 100, screen)
        show_text("Click Anywhere To Restart", 255, 250, WHITE, 25, screen)
    clock.tick(FPS)
    pygame.display.update()
