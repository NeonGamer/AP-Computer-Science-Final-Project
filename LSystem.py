from StringBuilder import *
from pygameTurtle import pgTurtle

class Rules:
    def __init__(self, variable, rule, action, angle):
        self.variable = variable
        self.rule = rule
        self.action = action
        self.angle = angle

def ApplyRules(stringB, rules):
  sb = StringBuilder()
  for ch in stringB.ToString():
    for i in rules:
      if ch == i.variable:
        sb.Append(i.rule)
  return sb

def DrawString(axiom, rules, iterations):
    sb = StringBuilder()
    sb.Append(axiom)
    for _ in range(iterations):
      sb = ApplyRules(sb, rules)
    return sb.ToString()

def DrawFractal(tur, axiom, rules, size, iterations):
    cachedPos = []
    cachedRot = []
    cachedSizes = []
    currentSize = size
    instructions = DrawString(axiom, rules, iterations)
    for ch in instructions:
        for currRule in rules:
            if ch == currRule.variable:
                if currRule.action == 'Forward':
                    tur.Forward(currentSize)
                elif currRule.action == 'Left':
                    tur.Left(currRule.angle)
                elif currRule.action == 'Right':
                    tur.Right(currRule.angle)
                elif currRule.action == 'CachePos':
                    cachedPos.append(tur.current_pos)
                    cachedRot.append(tur.current_rot)
                elif currRule.action == 'SetPosFromCache':
                    tur.PenUp()
                    tur.SetPos(cachedPos.pop(-1))
                    tur.SetRot(cachedRot.pop(-1))
                    tur.PenDown()
                elif currRule.action == 'SetSize':
                    cachedSizes.append(currentSize)
                    currentSize = currRule.angle
                elif currRule.action == 'AddToSize':
                    cachedSizes.append(currentSize)
                    currentSize += currRule.angle
                elif currRule.action == 'SubFromSize':
                    cachedSizes.append(currentSize)
                    currentSize -= currRule.angle
                elif currRule.action == 'MulSize':
                    cachedSizes.append(currentSize)
                    currentSize *= currRule.angle
                elif currRule.action == 'RestoreSize':
                    currentSize = cachedSizes.pop(-1)