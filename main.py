import os
import random
os.system("clear")

class Board():
    def __init__(self) :
      self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("--------------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("--------------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player): 
      if self.cells[cell_no] == " ":
        self.cells[cell_no] = player

    def is_winner(self, player):

      result = True
      for cell_no in [1,2,3]:
          if self.cells[cell_no] != player:
              result = False

      if result == True:
          return True

      if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
          return True
      if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
          return True
      if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
          return True
      if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
          return True
      if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
          return True
      if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
          return True
      if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
          return True
      if self.cells[7]==player and self.cells[5]==player and self.cells[3]==player:
          return True

      return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False


    def reset(self):
      self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


    def ai_move(self,player):

      if player == "X":
          enemy = "O"

      if player == "O":
          enemy = "X"

      #If the centre is open choose thar
      if self.cells[5] == " ":
          self.update_cell(5, player)

      #AI Can win
      

      #AI Blocks


      #Choose random
      for i in range(1,10):
          if self.cells[i] == " ":
              self.update_cell(i,player)
              break


      rand = list(range(1,10))
      random.shuffle(rand)
      for x in rand:
            if self.cells[x] == " ":
                self.update_cells(x, player)   
                break




board = Board()
board.display()

def print_header():
    print("Welcome to TicTacToe\n")

#Refresh the screen
#Then print the header
#Show Board
def refresh_screen():
    os.system("clear")

    print_header()

    board.display()

while True:
    refresh_screen()

#Get the X input
    x_choice = int(input("\nX) Please choose 1 - 9. > "))

# Update board
    board.update_cell(x_choice , "X")

#Refresh screen function
    refresh_screen()

# Check for X winner
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

# Check for tie game
    if board.is_tie():
        print("\nTie Game!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break


#Get the 0 input
    o_choice = int(input("\nO) Please choose 1 - 9. > "))

    board.ai_move("O")

    refresh_screen()


# Update board
    board.update_cell(o_choice , "O")

    refresh_screen()


# Check for O winner
    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

# Check for tie game
    if board.is_tie():
        print("\nTie Game!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break