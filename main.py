import pygame
import os ,sys, json

pygame.init()

settingsFile = os.path.join("settings.cfg")
with open("settings.cfg", "r") as jsonFile:
    data = json.load(jsonFile)
    imgSize = data["imgScale"]
    screenSize = data["screenSize"]
    pathOfIMG = data["pathOfImg"]
    whichMic = data["whichMic"]
    maxFPS= data["maxFPS"]
    frequency= data["frequency"]
    amplitube= data["amplitube"]



    jsonFile.close()
    
screen = pygame.display.set_mode((screenSize , screenSize))

img = pygame.image.load(pathOfIMG)
clock = pygame.time.Clock()

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    img = pygame.transform.scale(img ,(imgSize,imgSize))
    
    screen.blit(img , ((screenSize/2)-(imgSize/2),(screenSize/2)- (imgSize/2)))
    pygame.display.flip()
    clock.tick(maxFPS)
pygame.quit()

