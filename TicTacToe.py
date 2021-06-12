#!/usr/bin/python3


#Description        :   Multiplayer TicTacToe game. Runs on a single console. 
#                       Waits for Users to enter Cell address and makes a mark.
#Last Updated       :   2020-04-21
#@author            :   Shreehari Lele
#@authorContact     :   shreeharil@gmail.com
#License Description:   GNU General Public License v3.0


def disp():
  print ("**********")
  print ("""     A   B    C
     -   -    -
1|   {} |  {} |  {}
  ----------------
2|   {} | {}  |  {}
  ----------------
3|   {} |  {} |  {}
""".format(PositionedValues[0],
PositionedValues[1],
PositionedValues[2],
PositionedValues[3],
PositionedValues[4],
PositionedValues[5],
PositionedValues[6],
PositionedValues[7],
PositionedValues[8]))
  print ("**********")


possibleValues=['X','0']
validPositions=['A1','B1','C1','A2','B2','C2','A3','B3','C3']
PositionedValues=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def validatePosition(boardPosition,playerId):
  if boardPosition in validPositions:
    index = validPositions.index(boardPosition)
    #Cant pop since position is important
    validPositions[index]=boardPosition+possibleValues[playerId]
    PositionedValues[index]=possibleValues[playerId]
    print (validPositions)
    return True;
  return False

def checkVictory(boardPosition,playerId):
  hoffset=0
  voffset=0
  if 'B' in boardPosition:
    hoffset=1
  elif 'C' in boardPosition:
    hoffset=2
  if '2' in boardPosition:
    voffset=3
  elif '3' in boardPosition:
    voffset=6
  pos=0
  if (possibleValues[playerId] in validPositions[hoffset]
      and possibleValues[playerId] in validPositions[hoffset+3]
      and possibleValues[playerId] in validPositions[hoffset+6]):
    return True
  if (possibleValues[playerId] in validPositions[voffset]
      and possibleValues[playerId] in validPositions[voffset+1]
      and possibleValues[playerId] in validPositions[voffset+2]):
    return True
  if (possibleValues[playerId] in validPositions[0]
      and possibleValues[playerId] in validPositions[4]
      and possibleValues[playerId] in validPositions[8]):
      return True
  if (possibleValues[playerId] in validPositions[2]
      and possibleValues[playerId] in validPositions[4]
      and possibleValues[playerId] in validPositions[6]):
    return True
  return False;

def main():
  print("Hari Om World")
  disp()
  i=1
  for x in range (0,9):
    i=(i+1)%2
    print ("Player"+str(i+1))
    userin = input("Enter a position ")
    if(False == validatePosition(userin,i)):
      print("Position not empty")
      x=x-1
      i = i-1
    else:
      disp()
    if(checkVictory(userin,i)):
      print ("##**##**##**")
      print ("  Player"+str(i+1)+" has won!")
      print("##**##**##**")
      break;
    if ' ' not in PositionedValues:
      print ("##**##**##**")
      print ("  Draw ")
      print("##**##**##**")
      break;


main()
