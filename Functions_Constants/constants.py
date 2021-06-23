import pygame,sys,os
from pygame.locals import *


pygame.init()

Clock=pygame.time.Clock()
FPS= 60
pygame.display.set_caption("Maze Duel")
Width, Height = 1280,720
WIN=pygame.display.set_mode((Width,Height))

font=pygame.font.SysFont(None,30)

BLACK= (0,0,0) 
WHITE = (255,255,255) 
RED= (255,0,0)
BLUE=(0,0,255)

click=False

normal_size=(300,100)
enlarged_size=(380,120)

Background_image_unrefined= pygame.image.load(os.path.join("images","Main_Menu_Images","Background.png"))
Background=pygame.transform.scale(Background_image_unrefined,(Width,Height))

Blank_BG_unrefined= pygame.image.load(os.path.join("images","Main_Menu_Images","Blank_BG.png"))
Blank_BG=pygame.transform.scale(Blank_BG_unrefined,(Width,Height))

Button_play_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Play.png"))
Image_play=pygame.transform.scale(Button_play_unrefined,(normal_size))
Image_play_enlarged=pygame.transform.scale(Button_play_unrefined,(enlarged_size))

Button_options_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Options.png"))
Image_options=pygame.transform.scale(Button_options_unrefined,(normal_size))
Image_options_enlarged=pygame.transform.scale(Button_options_unrefined,(enlarged_size))

Button_exit_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Exit.png"))
Image_exit=pygame.transform.scale(Button_exit_unrefined,(normal_size))
Image_exit_enlarged=pygame.transform.scale(Button_exit_unrefined,(enlarged_size))

Button_fullscreen_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Fullscreen.png"))
Image_fullscreen=pygame.transform.scale(Button_fullscreen_unrefined,(normal_size))
Image_fullscreen_enlarged=pygame.transform.scale(Button_fullscreen_unrefined,(enlarged_size))

Button_login_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Login.png"))
Image_login=pygame.transform.scale(Button_login_unrefined,(normal_size))
Image_login_enlarged=pygame.transform.scale(Button_login_unrefined,(enlarged_size))

Button_back_unrefined=pygame.image.load(os.path.join("images","Main_Menu_Images","Button_Back.png"))
Image_back=pygame.transform.scale(Button_back_unrefined,(180,80))
Image_back_enlarged=pygame.transform.scale(Button_back_unrefined,(190,90))


Button_bg_unrefined=pygame.image.load(os.path.join("images","Text_Bg.png"))
Button_bg=pygame.transform.scale(Button_bg_unrefined,(220,80))
