import pygame,sys,os
from pygame.locals import *
import Transition_moving

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

            button_play=WIN.blit(Button_bg,(35,400))
            button_options=WIN.blit(Button_bg,(35,500))
            button_exit=WIN.blit(Button_bg,(35,600))


            if button_play.collidepoint((bonk)):
                if click==True:
                    play_pressed()
                    
            if button_options.collidepoint((bonk)):
                if click==True:
                    options_pressed()

            draw_text("Play",font,BLACK,WIN,50,425)
            draw_text("Options",font,BLACK,WIN,50,525)
            draw_text("Exit game",font,BLACK,WIN,50,625)

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
        
        draw_text("Play",font,BLUE,WIN,20,20)
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

        button_fullscreen=WIN.blit(Button_bg,(35,600))
        button_login=WIN.blit(Button_bg,(35,500))



        draw_text("User Login",font,BLACK,WIN,50,525)
        draw_text("Toggle fullscreen",font,BLACK,WIN,50,625)
        draw_text("Options",font,BLUE,WIN,20,20)
        
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
        draw_text("Login screen",font,BLUE,WIN,20,20)

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