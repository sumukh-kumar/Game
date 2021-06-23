import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving

pygame.init()



def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def main_menu():
    while True:
            constants.WIN.blit(constants.Background,(0,0))

            mx,my=pygame.mouse.get_pos()
            bonk=(mx,my)

            button_play=constants.WIN.blit(constants.Image_play,(35,300))
            button_options=constants.WIN.blit(constants.Image_options,(35,450))
            button_exit=constants.WIN.blit(constants.Image_exit,(35,600))


            if button_play.collidepoint((bonk)):
                constants.WIN.blit(constants.Background,(0,0))
                button_options=constants.WIN.blit(constants.Image_options,(35,450))
                button_exit=constants.WIN.blit(constants.Image_exit,(35,600))
                button_play=constants.WIN.blit(constants.Image_play_enlarged,(35,300))
                if click==True:
                    play_pressed()
                    
            if button_options.collidepoint((bonk)):
                constants.WIN.blit(constants.Background,(0,0))
                button_options=constants.WIN.blit(constants.Image_options_enlarged,(35,450))
                button_exit=constants.WIN.blit(constants.Image_exit,(35,600))
                button_play=constants.WIN.blit(constants.Image_play,(35,300))
                if click==True:
                    options_pressed()

            if button_exit.collidepoint((bonk)):
                    constants.WIN.blit(constants.Background,(0,0))
                    button_exit=constants.WIN.blit(constants.Image_exit_enlarged,(35,600))
                    button_play=constants.WIN.blit(constants.Image_play,(35,300))
                    button_options=constants.WIN.blit(constants.Image_options,(35,450))

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
            constants.Clock.tick(constants.FPS)


def play_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        
        constants.WIN.blit(constants.Background,(0,0))


        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)



        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False

        pygame.display.update()
        constants.Clock.tick(constants.FPS)


def options_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        click=False
        constants.WIN.blit(constants.Blank_BG,(0,0))

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        button_fullscreen=constants.WIN.blit(constants.Image_fullscreen,(35,400))
        button_login=constants.WIN.blit(constants.Image_login,(35,575))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))



        if button_fullscreen.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen_enlarged,(35,400))
            constants.WIN.blit(constants.Image_login,(35,575))
            button_back=constants.WIN.blit(constants.Image_back,(10,5))
        
        if button_login.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_login_enlarged,(35,575))
            button_fullscreen=constants.WIN.blit(constants.Image_fullscreen,(35,400))
            button_back=constants.WIN.blit(constants.Image_back,(10,5))

        if button_back.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen,(35,400))
            constants.WIN.blit(constants.Image_login,(35,575))
            constants.WIN.blit(constants.Image_back_enlarged,(10,5))

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
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
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        running=False


        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def fullscreen_pressed():
    pygame.display.toggle_fullscreen()
    pygame.display.update()
    constants.Clock.tick(constants.FPS)

def login_pressed():
    running=True
    while running:
        constants.WIN.blit(constants.Background,(0,0))


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
        constants.Clock.tick(constants.FPS)


main_menu()