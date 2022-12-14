import math
import pygame

def RotateAboutPoint(angle, point1, originPoint):
  angle = (math.pi/180) * angle
  newX = math.cos(angle)*(point1[0]-originPoint[0])-math.sin(angle)*(point1[1]-originPoint[1])+originPoint[0]
  newY = math.sin(angle)*(point1[0]-originPoint[0])+math.cos(angle)*(point1[1]-originPoint[1])+originPoint[1]
  return (newX, newY)

class pgTurtle():
  def __init__(self, screen):
    #=====Turtle Position And Rotation Info=====
    self.pyScreen = screen
    self.current_pos = (self.pyScreen.get_width()/2, self.pyScreen.get_height()/2) #Default Position ( Middle of the window )
    self.current_rot = 180 #Default Rotation ( 180 is default, facing up )
    self.pen_state = True #Default Pen State ( Penup should be true be default )
    self.PenThickness = 1 #Default Pen Thickness
    self.PenColor = (0,0,0) #Default Pen Color ( Color = Black )
    self.postionLog = [] #This array will hold all of the positions of the turtle on the screen
  #=====Movement Funcs=====
  def Forward(self, distance: int):
    oldPos = self.current_pos
    self.current_pos = RotateAboutPoint(self.current_rot, (self.current_pos[0], self.current_pos[1]+distance), self.current_pos )
    if self.pen_state == True:
      pygame.draw.line(self.pyScreen, self.PenColor, oldPos, self.current_pos, self.PenThickness)
    self.postionLog.append(self.current_pos)
  def Right(self, angle: int): #Turn the turtle (angle) degrees to the right
     self.current_rot += angle
  def Left(self, angle: int): #Turn the turtle (angle) degrees to the left
     self.current_rot -= angle
  def SetPos(self, newPos: tuple): #Force set the position of the turtle
    oldPos = self.current_pos
    self.current_pos = newPos
    if self.pen_state == True:
      pygame.draw.line(self.pyScreen, self.PenColor, oldPos, self.current_pos, self.PenThickness)
    self.postionLog.append(self.current_pos)
  def SetRot(self, newRot: int): #Force set the rotation of the turtle
    self.current_rot = newRot
  #=====Drawing Funcs=====
  def PenUp(self): #Tell the turtle of start drawing
    self.pen_state = False
  def PenDown(self): #Tell the turtle of stop drawing
    self.pen_state = True
  def Circle(self, radius: int, fill: bool):
    if fill == True:
      pygame.draw.circle(self.pyScreen, self.PenColor, self.current_pos, radius)
  def PenThickness(self, newThickness): #Set the pen thickness
    self.Thickness = newThickness
  def PenColor(self, newColor): #Set the color of the prn color
    self.PenColor = newColor
