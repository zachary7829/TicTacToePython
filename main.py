#Zachary Keffaber 2/15/2021 to 2/16/2020, TicTacToe
import os
import sys
import time
import random
from random import randint


FirstLine = "123"
SecondLine = "456"
ThirdLine = "789"

Won = 0
def configdisplay():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print("  123")
  DisplayFirstLine = FirstLine.replace("1", "-")
  DisplayFirstLine = DisplayFirstLine.replace("2", "-")
  DisplayFirstLine = DisplayFirstLine.replace("3", "-")
  DisplaySecondLine = SecondLine.replace("4", "-")
  DisplaySecondLine = DisplaySecondLine.replace("5", "-")
  DisplaySecondLine = DisplaySecondLine.replace("6", "-")
  DisplayThirdLine = ThirdLine.replace("7", "-")
  DisplayThirdLine = DisplayThirdLine.replace("8", "-")
  DisplayThirdLine = DisplayThirdLine.replace("9", "-")
  print("A " + DisplayFirstLine)
  print("B " + DisplaySecondLine)
  print("C " + DisplayThirdLine)
  print("")
  return;

while Won == 0:
 configdisplay()
 letter = str(input("Input the letter where you want to place your X: "))
 letter = letter.capitalize()
 if letter != "A":
   if letter != "B":
    if letter != "C":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("Select a valid letter.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
 number = str(input("Input the number where you want to place your X: "))
 if number != "1":
   if number != "2":
    if number != "3":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("Select a valid number.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
 if letter == "A":
   FirstLine = FirstLine.replace(number, "X")
 if letter == "B":
   number = int(number)
   numberid = str(number + 3)
   SecondLine = SecondLine.replace(numberid, "X")
 if letter == "C":
   number = int(number)
   numberid = str(number + 6)
   ThirdLine = ThirdLine.replace(numberid, "X")
 #Bot chooses a place now
 masterline = FirstLine + SecondLine + ThirdLine
 result = masterline
 while masterline == result:
   number = int(number)
   if number < 3:
     number = 0 + randint(0, 1)
   if number >= 3:
     number = 0 - randint(0, 1)
   numberid = randint(1, 3)
   if numberid == 1:
     letter = "A"
   if numberid == 2:
     letter = "B"
   if numberid == 3:
     letter = "C"
   number = str(number)
   print(numberid)
   if letter == "A":
     FirstLine = FirstLine.replace(number, "O")
   if letter == "B":
     number = int(number)
     numberid = str(number + 3)
     SecondLine = SecondLine.replace(numberid, "O")
   if letter == "C":
     number = int(number)
     numberid = str(number + 6)
     ThirdLine = ThirdLine.replace(numberid, "O")
   result = FirstLine + SecondLine + ThirdLine
   if result == masterline:
     while masterline == result:
       number = randint(1, 3)
       numberid = randint (1, 3)
       if numberid == 1:
         letter = "A"
       if numberid == 2:
         letter = "B"
       if numberid == 3:
         letter = "C"
       number = str(number)
       if letter == "A":
         FirstLine = FirstLine.replace(number, "O")
       if letter == "B":
         number = int(number)
         numberid = str(number + 3)
         SecondLine = SecondLine.replace(numberid, "O")
       if letter == "C":
         number = int(number)
         numberid = str(number + 6)
         ThirdLine = ThirdLine.replace(numberid, "O")
       result = FirstLine + SecondLine + ThirdLine
   configdisplay()
 #Checks to see if player has won or lost yet
 if FirstLine == "XXX":
    Won = 1
 if SecondLine == "XXX":
    Won = 1
 if ThirdLine == "XXX":
    Won = 1
 OneLine = FirstLine[0] + SecondLine[0] + ThirdLine[0]
 if OneLine == "XXX":
    Won = 1
 OneLine = FirstLine[1] + SecondLine[1] + ThirdLine[1]
 if OneLine == "XXX":
    Won = 1
 OneLine = FirstLine[2] + SecondLine[2] + ThirdLine[2]
 if OneLine == "XXX":
    Won = 1
 OneLine = FirstLine[0] + SecondLine[1] + ThirdLine[2]
 if OneLine == "XXX":
    Won = 1
 OneLine = FirstLine[2] + SecondLine[1] + ThirdLine[0]
 if OneLine == "XXX":
    Won = 1
 if Won == 0:
   if FirstLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   if SecondLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   if ThirdLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   OneLine = FirstLine[0] + SecondLine[0] + ThirdLine[0]
   if OneLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   OneLine = FirstLine[1] + SecondLine[1] + ThirdLine[1]
   if OneLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   OneLine = FirstLine[2] + SecondLine[2] + ThirdLine[2]
   if OneLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   OneLine = FirstLine[0] + SecondLine[1] + ThirdLine[2]
   if OneLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
   OneLine = FirstLine[2] + SecondLine[1] + ThirdLine[0]
   if OneLine == "OOO":
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print("You have lost.")
      time.sleep(1)
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      os.execl(sys.executable, sys.executable, *sys.argv)
 

print("Congrats! You have won!")