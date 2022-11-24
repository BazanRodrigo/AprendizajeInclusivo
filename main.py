import pygame
import sys
from pygame.locals import *

def selectlenguaje(position):
    if (position[0] >= 50) and (position[0] <= 319) and (position[1] >= 100) and (position[1] <= 228):
        return('c')        
    if (position[0] >= 370) and (position[0] <= 639) and (position[1] >= 100) and (position[1] <= 228):
        return('java')
    if (position[0] >= 200) and (position[0] <= 469) and (position[1] >= 280) and (position[1] <= 408):
        return('python')


def main():
    pygame.init()
    tamaño=720, 480
    pantalla = pygame.display.set_mode(tamaño)
    pygame.display.set_caption("Programing")
    fondo = pygame.image.load('wallpaper.jpg')
    botonc = pygame.image.load('c.jpg')
    botonpython = pygame.image.load('python.jpg')
    botonjava = pygame.image.load('jave.jpg')    
    tiposvariablesc = pygame.image.load('tipos_ c.png')
    jugar = pygame.image.load('jugar.jpg')
    estructurajava = pygame.image.load('estructurajava.png')
    tiposjava = pygame.image.load('tipos java.png')
    tipospython = pygame.image.load('typepython.jpg')
    fondocvariables = pygame.image.load('fondocvariables.jpg')
    enterjugar = pygame.image.load('enterjugar.jpg')

    pantalla.blit(fondo,(0,0))    
    pantalla.blit(botonc, (50,100))
    pantalla.blit(botonjava, (370,100))
    pantalla.blit(botonpython, (200,280))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                ls = selectlenguaje(position)
                if(ls == 'c'):
                    pantalla.blit(fondocvariables,(0,0))                    
                    pantalla.blit(enterjugar,(400,50))
                    if event.type == pygame.K_KP_ENTER:
                        print('af')
                        pantalla.blit(fondo,(0,0))                    

                if(ls == 'java'):
                    pantalla.blit(fondo,(0,0))
                    pantalla.blit(estructurajava,(20,20))
                    pantalla.blit(tiposjava,(300,20))
                    pantalla.blit(jugar,(400,300))
                if(ls == 'python'):
                    pantalla.blit(fondo,(0,0))
                    pantalla.blit(tipospython,(20,20))                    
                    pantalla.blit(jugar,(400,300))

        pygame.display.update()

if __name__ == "__main__":
    main()