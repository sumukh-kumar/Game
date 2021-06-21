import pygame,sys,os
from pygame.locals import *
import Transition_moving

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

normal_size=(300,130)
enlarged_size=(330,160)

Background_image_unrefined= pygame.image.load(os.path.join("images","Standard.png"))
Background=pygame.transform.scale(Background_image_unrefined,(Width,Height))

Button_play_unrefined=pygame.image.load(os.path.join("images","Buttonplay.png"))
Image_play=pygame.transform.scale(Button_play_unrefined,(normal_size))
Image_play_enlarged=pygame.transform.scale(Button_play_unrefined,(enlarged_size))

Button_options_unrefined=pygame.image.load(os.path.join("images","Buttonoptions.png"))
Image_options=pygame.transform.scale(Button_options_unrefined,(normal_size))
Image_options_enlarged=pygame.transform.scale(Button_options_unrefined,(enlarged_size))

Button_exit_unrefined=pygame.image.load(os.path.join("images","Buttonexit.png"))
Image_exit=pygame.transform.scale(Button_exit_unrefined,(normal_size))
Image_exit_enlarged=pygame.transform.scale(Button_exit_unrefined,(330,145))

Button_fullscreen_unrefined=pygame.image.load(os.path.join("images","Buttonfullscrn.png"))
Image_fullscreen=pygame.transform.scale(Button_fullscreen_unrefined,(normal_size))
Image_fullscreen_enlarged=pygame.transform.scale(Button_fullscreen_unrefined,(enlarged_size))

Button_login_unrefined=pygame.image.load(os.path.join("images","Login.png"))
Image_login=pygame.transform.scale(Button_login_unrefined,(normal_size))
Image_login_enlarged=pygame.transform.scale(Button_login_unrefined,(enlarged_size))

Button_back_unrefined=pygame.image.load(os.path.join("images","Buttonback.png"))
Image_back=pygame.transform.scale(Button_back_unrefined,(160,100))


Button_bg_unrefined=pygame.image.load(os.path.join("images","Text_Bg.png"))
Button_bg=pygame.transform.scale(Button_bg_unrefined,(220,80))



def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def main_menu():
    while True:
            WIN.blit(Background,(0,0))
            draw_text("",font,WHITE,WIN,20,20)

            mx,my=pygame.mouse.get_pos()
            bonk=(mx,my)

            button_play=WIN.blit(Image_play,(35,300))
            button_options=WIN.blit(Image_options,(35,450))
            button_exit=WIN.blit(Image_exit,(35,600))


            if button_play.collidepoint((bonk)):
                WIN.blit(Background,(0,0))
                button_options=WIN.blit(Image_options,(35,450))
                button_exit=WIN.blit(Image_exit,(35,600))
                button_play=WIN.blit(Image_play_enlarged,(35,300))
                if click==True:
                    play_pressed()
                    
            if button_options.collidepoint((bonk)):
                WIN.blit(Background,(0,0))
                button_options=WIN.blit(Image_options_enlarged,(35,450))
                button_exit=WIN.blit(Image_exit,(35,600))
                button_play=WIN.blit(Image_play,(35,300))
                if click==True:
                    options_pressed()

            if button_exit.collidepoint((bonk)):
                    WIN.blit(Background,(0,0))
                    button_exit=WIN.blit(Image_exit_enlarged,(35,600))
                    button_play=WIN.blit(Image_play,(35,300))
                    button_options=WIN.blit(Image_options,(35,450))

            click=False

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
                if button_exit.collidepoint((bonk)):
                    if click==True:
                        click=False
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()
            Clock.tick(FPS)


def play_pressed():
    running=True
    Transition_moving.fadetoblack(Width,Height)
    Transition_moving.fadetoscreen(Width,Height)
    while running:
        
        WIN.blit(Background,(0,0))
        #draw_text("Play",font,BLUE,WIN,20,20)

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)



        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    Transition_moving.fadetoblack(Width,Height)
                    Transition_moving.fadetoscreen(Width,Height)
                    running=False

        pygame.display.update()
        Clock.tick(FPS)


def options_pressed():
    running=True
    Transition_moving.fadetoblack(Width,Height)
    Transition_moving.fadetoscreen(Width,Height)
    while running:
        click=False
        WIN.blit(Background,(0,0))

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        button_fullscreen=WIN.blit(Image_fullscreen,(35,400))
        button_login=WIN.blit(Image_login,(35,575))
        button_back=WIN.blit(Image_back,(-10,5))



        if button_fullscreen.collidepoint((bonk)):
            WIN.blit(Background,(0,0))
            WIN.blit(Image_fullscreen_enlarged,(35,400))
            WIN.blit(Image_login,(35,575))
            button_back=WIN.blit(Image_back,(-10,5))
        
        if button_login.collidepoint((bonk)):
            WIN.blit(Background,(0,0))
            WIN.blit(Image_login_enlarged,(35,575))
            button_fullscreen=WIN.blit(Image_fullscreen,(35,400))
            button_back=WIN.blit(Image_back,(-10,5))


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    Transition_moving.fadetoblack(Width,Height)
                    Transition_moving.fadetoscreen(Width,Height)
                    running=False
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
            if button_fullscreen.collidepoint((bonk)):
                if click==True:
                    fullscreen_pressed()
            if button_login.collidepoint((bonk)):
                if click==True:
                    login_pressed()
            if button_back.collidepoint((bonk)):
                if click==True:
                        Transition_moving.fadetoblack(Width,Height)
                        Transition_moving.fadetoscreen(Width,Height)
                        running=False


        pygame.display.update()
        Clock.tick(FPS)

def fullscreen_pressed():
    pygame.display.toggle_fullscreen()
    pygame.display.update()
    Clock.tick(FPS)

def login_pressed():
    running=True
    while running:
        WIN.blit(Background,(0,0))


        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False

        pygame.display.update()
        Clock.tick(FPS)


main_menu()