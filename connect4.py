from time import sleep
from termcolor import colored
import os

class Cell:
  def __init__(self,who = None):
    self.occupied = False;
    if who is None or who is "R" or who is "B":
      self.who = who;
    else:
      raise ValueError("Invalid Player Type")
      
  def __str__(self):
    if (self.who == "R"):
      return '🔴'
    elif (self.who == "B"):
      return '🔵'
    else:
      return '⭕'

  def setWho(self, who):
    self.who = who

class Board:
  def __init__(self,col=7,row=6):
    if(col < 4 or row < 4):
      raise ValueError("Can not have less than 6x7")
    self.Player = True
    self.Max = col*row
    self.count = 0
    self.grid = []
    self.row = int(row)
    self.col = int(col)
    self.letters = []
    for i in range(self.col):
      self.letters.append(chr(ord('A')+i))
    
    for i in range(row):
        self.grid.append([])
        for j in range(col):
          self.grid[i].append(Cell())
            # if((i)%3==0):
            #   c = Cell()
            # elif((i)%3==1):
            #   c = Cell("R")
            # else:
            #   c = Cell("B")
            # self.grid[i].append(c)
            
  def __str__(self):
    out = " " 
    for i in range(len(self.letters)):
      if(i%2==0 and i > 0): 
        out += "{:^3s}".format(self.letters[i])
      else:
        out += "{:^2s}".format(self.letters[i])
    out += "\n"
    for i in range(self.row):
      for j in range(self.col):
        c = str(self.grid[i][j])
        out += "{:^s}".format(c)
      out += "\n"
    return out
  
  def clearGame(self):
    for i in range(self.row):
        for j in range(self.col):
          self.grid[i][j] = Cell()
          
  def addDisc(self, c, p):
    col = ord(c)-ord('A')
    if(self.grid[0][col].who == "R" or self.grid[0][col].who == "B"):
      return False
    for i in range(self.row-1,-1,-1):
      if(self.grid[i][col].who is None):
        if (p):
          self.grid[i][col].who = "R"
          return True
        else:
          self.grid[i][col].who = "B"
          return True
  
  def checkGame(self):
    for row in range(self.row-3):
      for col in range(self.col-3):
        a,b,c,d = row,row+1,row+2,row+3
        e,f,g,h = col,col+1,col+2,col+3
        # print(a,b,c,d)
        # print(e,f,g,h)
        
        # COL 1
        w1 = self.grid[a][e].who 
        w2 = self.grid[b][e].who
        w3 = self.grid[c][e].who
        w4 = self.grid[d][e].who
        
        # COL 2
        w5 = self.grid[a][f].who
        w6 = self.grid[b][f].who  
        w7 = self.grid[c][f].who
        w8 = self.grid[d][f].who
        
        # COL 3
        w9 = self.grid[a][g].who
        w10 = self.grid[b][g].who
        w11 = self.grid[c][g].who
        w12 = self.grid[d][g].who
        
        # COL 4
        w13 = self.grid[a][h].who
        w14 = self.grid[b][h].who
        w15 = self.grid[c][h].who
        w16 = self.grid[d][h].who
        
        # print(w16)
        
        # print(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16)
        
        # print(w1 == w2 == w3 == w4)
        
        #A1-4
        if (w1 == w2 == w3 == w4) and w1 is not None:
          print("WINNER!")
          return True
        
        #B1-4
        if (w5 == w6 == w7 == w8) and w5 is not None:
          print("WINNER!")
          return True
        
        #C1-4
        if (w9 == w10 == w11 == w12) and w9 is not None:
          print("WINNER!")
          return True
        
        #D1-4
        if (w13 == w14 == w15 == w16) and w13 is not None:
          print("WINNER!")
          return True
          
        #A-D1
        if (w1 == w5 == w9 == w13) and w1 is not None:
          print("WINNER!")
          return True
        
        #A-D2
        if (w2 == w6 == w10 == w14) and w2 is not None:
          print("WINNER!")
          return True
        
        #A-D3
        if (w3 == w7 == w11 == w15) and w3 is not None:
          print("WINNER!")
          return True
        
        #A-D4
        if (w4 == w8 == w12 == w16) and w1 is not None:
          print("WINNER!")
          return True
        
        # A1,B2,C3,D4
        if (w1 == w6 == w11 == w16)  and w1 is not None:
          print("WINNER!")
          return True
        
        # A4,B3,C2,D1
        if (w4 == w7 == w10 == w13)  and w1 is not None:
          print("WINNER!")
          return True
        
    return False #Checks if Someone won the Game

class Game:
  def __init__(self):
    self.b = Board()             
    self.playGame()
    
  def playGame(self):
    while True:
      os.system('cls')
      print(self.b)
      if (self.b.Player):
        print(colored("Red","red"))
      else:
        print(colored("Blue","blue"))
      s = input()
      s = s.upper()
      if s in self.b.letters:
        if(self.b.addDisc(s,self.b.Player)):
          self.b.count += 1
          self.b.Player = not self.b.Player
          if(self.b.checkGame()):
            break
        #os.system('cls')
        # sleep(.100)
      if (s == "Quit!"):
        break;
    print("End of Game") #Runs the Game

Gme = Game()
sleep(.2)
os.system('cls')
print(Gme.b)
print("Winner!")
