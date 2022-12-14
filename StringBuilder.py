from io import StringIO

#==================================================
# String Builder
# Faster than normally adding to a string
#==================================================
class StringBuilder():
  def __init__(self):
    self.stringBuilder = StringIO()
  def Append(self, text):
    self.stringBuilder.write(text)
  def Clear(self):
    self.stringBuilder.reset()
  def ToString(self):
    return self.stringBuilder.getvalue()
