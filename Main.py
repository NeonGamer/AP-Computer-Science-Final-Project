import math
import pygame
import sys
from pygameTurtle import *
from LSystem import *
from ButtonHandler import *
from LoadTextures import *

#===================================
# Basic Window Setup and setting up screen for fractal rendering
#===================================
pygame.init()

(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
fractalsScreen = screen.copy()
buttonsScreen = screen.copy()
clock = pygame.time.Clock()
(xScale, yScale) = (800, 800)
(xOffset, yOffset) = (0, 0)
running = True

testT = 2

(minX, minY, maxX, maxY)= (0,0,0,0)

#===================================
# Fractal Presets
#===================================
def ClearScreen():
    fractalsScreen.fill((200,200,200))

def DragonsCurve():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'F+G', 'Forward', 0))
    rulesList.append( Rules('G', 'F-G', 'Forward', 0))
    rulesList.append( Rules('+', '+', 'Right', 90))
    rulesList.append( Rules('-', '-', 'Left', 90))
    DrawFractal(newTurtle, 'F', rulesList, 1, 18)

def KoshCurve_a():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'FF+F+F+F+F+F-F', 'Forward', 0))
    rulesList.append( Rules('+', '+', 'Right', 90))
    rulesList.append( Rules('-', '-', 'Left', 90))
    DrawFractal(newTurtle, 'F+F+F+F', rulesList, 1, 4)
def KoshCurve_b():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'FF+F+F+F+FF', 'Forward', 0))
    rulesList.append( Rules('+', '+', 'Right', 90))
    rulesList.append( Rules('-', '-', 'Left', 90))
    DrawFractal(newTurtle, 'F+F+F+F', rulesList, 1, 4)
def KoshCurve_c():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'FF+F-F+F+FF', 'Forward', 0))
    rulesList.append( Rules('+', '+', 'Right', 90))
    rulesList.append( Rules('-', '-', 'Left', 90))
    DrawFractal(newTurtle, 'F+F+F+F', rulesList, 2.5, 5)
def KoshSnoflake():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'F-F++F-F', 'Forward', 0))
    rulesList.append( Rules('+', '+', 'Right', 60))
    rulesList.append( Rules('-', '-', 'Left', 60))
    rulesList.append( Rules('g', 'g', 'Right', 120))
    DrawFractal(newTurtle, 'FgFgF', rulesList, .5, 6)

def TreeFractal():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('B', 'F[M-BR][M+BR]', 'Forward', 0))
    rulesList.append( Rules('F', 'F', 'Forward', 0))
    rulesList.append( Rules('[', '[', 'CachePos', 0))
    rulesList.append( Rules(']', ']', 'SetPosFromCache', 0))
    rulesList.append( Rules('+', '+', 'Right', 45* math.pow(math.sin(pygame.time.get_ticks()/1000), 2) ))
    rulesList.append( Rules('-', '-', 'Left', 45* math.pow(math.sin(pygame.time.get_ticks()/1000), 2) ))
    rulesList.append(Rules('M', 'M', 'MulSize', .7))
    rulesList.append(Rules('R', 'R', 'RestoreSize', 0))
    DrawFractal(newTurtle, 'B', rulesList, 80, 11)

def FernFractal():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'FF', 'Forward', 0))
    rulesList.append( Rules('X', 'F+[[X]-X]-F[-FX]+X', '', 0))
    rulesList.append( Rules('[', '[', 'CachePos', 0))
    rulesList.append( Rules(']', ']', 'SetPosFromCache', 0))
    rulesList.append( Rules('+', '+', 'Right', 25))
    rulesList.append( Rules('-', '-', 'Left', 25 + math.sin(pygame.time.get_ticks()/1000)))
    DrawFractal(newTurtle, 'X', rulesList, 2, 6)

def BarsleyFernFractal():
    newTurtle = pgTurtle(fractalsScreen)
    fractalsScreen.fill((200,200,200))
    rulesList = []
    rulesList.append( Rules('F', 'F', 'Forward', 0))
    rulesList.append( Rules('B', '+FF[{MBPBPBPBPBPBPBPBPBPBPBPB]RRRRRRRRRRRR+F[}MBPBPBPBPBPBPBPBPBPBPBPB]RRRRRRRRRRRR', '', 0))

    rulesList.append( Rules('[', '[', 'CachePos', 0))
    rulesList.append( Rules(']', ']', 'SetPosFromCache', 0))

    rulesList.append( Rules('+', '+', 'Right', 5))
    rulesList.append( Rules('-', '-', 'Left', 5))

    rulesList.append(Rules('{', '{', 'Right', 45))
    rulesList.append(Rules('}', '}', 'Left', 45))

    rulesList.append(Rules('M', 'M', 'MulSize', .3))
    rulesList.append(Rules('P', 'P', 'MulSize', .8))
    rulesList.append(Rules('R', 'R', 'RestoreSize', 0))

    DrawFractal(newTurtle, 'BPBPBPBPBPBPBPBPBPBPBPB', rulesList, 30, 4)
    

#===================================
# Instancing Buttons and defining 'DrawButtons' function
#===================================
clearBtn = Button(clearTex_Normal, clearTex_Hover, clearTex_Click, screen.get_width()-110, 10, ClearScreen, screen)
dragonsCurveBtn = Button(dragonsCurveTex_Normal, dragonsCurveTex_Hover, dragonsCurveTex_Click, screen.get_width()-110, 70, DragonsCurve, screen)
koshCurveABtn = Button(KoshCurveATex_Normal, KoshCurveATex_Hover, KoshCurveATex_Click, screen.get_width()-110, 130, KoshCurve_a, screen)
koshCurveBBtn = Button(KoshCurveBTex_Normal, KoshCurveBTex_Hover, KoshCurveBTex_Click, screen.get_width()-110, 190, KoshCurve_b, screen)
koshCurveCBtn = Button(KoshCurveCTex_Normal, KoshCurveCTex_Hover, KoshCurveCTex_Click, screen.get_width()-110, 250, KoshCurve_c, screen)
koshSnowflakeBtn = Button(KoshSnowflake_Normal, KoshSnowflake_Hover, KoshSnowflake_Click, screen.get_width()-110, 310, KoshSnoflake, screen)

def DrawButtons():
    clearBtn.draw(True)
    dragonsCurveBtn.draw(True)
    koshCurveABtn.draw(True)
    koshCurveBBtn.draw(True)
    koshCurveCBtn.draw(True)
    koshSnowflakeBtn.draw(True)
#===================================
# Main Loop
#===================================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                testT += .1
            if event.key == pygame.K_s:
                testT -= .1
    screen.fill((200, 200, 200))
    #BarsleyFernFractal()
    fractalsScreen = pygame.transform.scale(fractalsScreen, (xScale, yScale))
    screen.blit(fractalsScreen, (((800-xScale)/2)+xOffset, ((800-yScale)/2)+yOffset))
    DrawButtons()
    clock.tick()
    fps = int(clock.get_fps())
    pygame.display.set_caption(f'Running at {fps} fps')
    pygame.display.flip()
  
