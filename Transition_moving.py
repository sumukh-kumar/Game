import pygame,os
from pygame.locals import *

pygame.init()

Clock=pygame.time.Clock()
FPS= 60
pygame.display.set_caption("Game")
Width, Height = 1280,720
WIN=pygame.display.set_mode((Width,Height))

font=pygame.font.SysFont(None,30)

BLACK= (0,0,0) 
WHITE = (255,255,255) 
RED= (255,0,0)
BLUE=(0,0,255)

click=False

Background_image_unrefined= pygame.image.load(os.path.join("images","Better.jpg"))
Background=pygame.transform.scale(Background_image_unrefined,(Width,Height))
Button_bg_unrefined=pygame.image.load(os.path.join("images","Text_Bg.png"))
Button_bg=pygame.transform.scale(Button_bg_unrefined,(223,60))


def fadetoblack(Width,Height): 
    fade = pygame.Surface((Width, Height))
    fade.fill((0,0,0))
    for alpha in range(0, 200):
        fade.set_alpha(alpha)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def fadetoscreen(Width,Height): 
    fade = pygame.Surface((Width, Height))
    fade.fill((0,0,0))
    for alpha in range(200, 0,-1):
        fade.set_alpha(alpha)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        WIN.blit(Background,(0,0))
        pygame.time.delay(1)