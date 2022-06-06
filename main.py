import pygame



pygame.init()
screen= pygame.display.set_mode((800,600))

background = pygame.image.load("spacecrafts.png")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invasion")

while True:
    screen.blit(background,(0,0))
    pygame.display.update()
