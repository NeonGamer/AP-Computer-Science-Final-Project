import pygame

class Button:
    def __init__(self, normal, hover, click, x, y, action, screen):
        self.normalTex = normal
        self.hoverTex = hover
        self.clickTex = click
        self.normalRect = self.normalTex.get_rect()
        self.hoverRect = self.hoverTex.get_rect()
        self.clickRect = self.clickTex.get_rect()
        self.normalRect.topleft = (x, y)
        self.hoverRect.topleft = (x, y)
        self.clickRect.topleft = (x, y)
        self.xPos = x
        self.yPos = y
        
        self.currentRect = self.normalRect
        self.currentImage = self.normalTex
        
        self.pyScreen = screen
        self.clicked = False
        self.action = action
    def draw(self, isActive):
        if isActive == True:
            pos = pygame.mouse.get_pos()
            if self.currentRect.collidepoint(pos):
                self.currentRect = self.hoverRect
                self.currentImage = self.hoverTex
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.action()
                if pygame.mouse.get_pressed()[0] == 1:
                    self.currentRect = self.clickRect
                    self.currentImage =self.clickTex
            if pygame.mouse.get_pressed()[0] == 0 and self.currentRect.collidepoint(pos) == False:
                    self.currentRect = self.normalRect
                    self.currentImage = self.normalTex    
            else:
                 if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
            self.pyScreen.blit(self.currentImage, (self.xPos, self.yPos))
       
        
