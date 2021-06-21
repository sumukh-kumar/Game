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

Background_image_unrefined= pygame.image.load(os.path.join("images","StandardBG.png"))
Background=pygame.transform.scale(Background_image_unrefined,(Width,Height))
Button_play_unrefined=pygame.image.load(os.path.join("images","Buttonplay.png"))
Image_play=pygame.transform.scale(Button_play_unrefined,(220,80))
Image_play_enlarged=pygame.transform.scale(Button_play_unrefined,(300,115))

Button_options_unrefined=pygame.image.load(os.path.join("images","Buttonoptions.png"))
Image_options=pygame.transform.scale(Button_options_unrefined,(220,80))
Image_options_enlarged=pygame.transform.scale(Button_options_unrefined,(300,105))

Button_exit_unrefined=pygame.image.load(os.path.join("images","Buttonexit.png"))
Image_exit=pygame.transform.scale(Button_exit_unrefined,(220,80))
Image_exit_enlarged=pygame.transform.scale(Button_exit_unrefined,(300,105))

Button_bg_unrefined=pygame.image.load(os.path.join("images","Text_Bg.png"))
Button_bg=pygame.transform.scale(Button_bg_unrefined,(220,80))


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