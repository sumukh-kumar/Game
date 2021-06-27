import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, mfunc

def name_input(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if constants.input_rect.collidepoint(event.pos):
            print(event.pos)
            constants.active = True
        else:
            constants.active = False

            
    if event.type==pygame.KEYDOWN:  
        if constants.active == True:
            if event.key==pygame.K_BACKSPACE:
                constants.charcount-=1
                constants.user_text = constants.user_text[:-1]
                constants.active = True
            else:
                if constants.charcount <= 10:
                    constants.user_text += event.unicode 
                    constants.charcount+=1

def pword_input(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if constants.pinput_rect.collidepoint(event.pos):
            print(event.pos)
            constants.pactive = True
        else:
            constants.pactive = False

            
    if event.type==pygame.KEYDOWN:  
        if constants.pactive == True:
            if event.key==pygame.K_BACKSPACE:
                constants.pcharcount-=1
                constants.puser_text = constants.puser_text[:-1]
                constants.pactive = True
            else:
                if constants.pcharcount <= 10:
                    constants.puser_text += event.unicode 
                    constants.pcharcount+=1