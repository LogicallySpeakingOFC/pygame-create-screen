import pygame, time
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sound")

soundObj = pygame.mixer.Sound("beep1.ogg")
soundObj.play()
time.sleep(1)
soundObj.stop()