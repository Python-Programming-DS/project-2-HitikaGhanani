
''' Hi, My name is Hitika Ghanani and below is the updated code for 'TIC TAC TOE'. 
I have build this game as a part of programming project. This is the improvised version where I applied Object Oreiented Programming using classes and objects. The game logic remains the same - in this game two player play it from the same keyboard in a 3x3 grid and each player get turn alternately. One player uses X and the other player uses O. If any player gets 3 consecutive X's or O's be it horizontally or vertically or diagonally that player wins.
'''

#creating Board class for building the Game Board:
class Board:

    # this constructor initiates the board with empty cells
    def __init__(self):
        self.c = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]


    # this method prints the board. Recall that class methods are functions
    def printBoard(self):
    # BOARD_HEADER constant
        BOARD_HEADER = "-----------------\n|R\\C| 0 | 1 | 2 |\n-----------------"
        print(BOARD_HEADER)


    # using a for-loop, it increments through the rows
        for i in range(3):
            print(f"| {i} | {self.c[i][0]} | {self.c[i][1]} | {self.c[i][2]} |")
            print("-----------------")
        print()

# define Game class to implement the Game Logic:
class Game:
# the constructor
    def __init__(self):
        self.board = Board()
        self.turn = 'X'
            
    # method to switch players
    def switchPlayer(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    # method to validate the user's entry
    def validateEntry(self, row,col):
        if (row <0 or row >2 or col <0 or col >2):
            print("Invalid entry: try again.")
            print("Row & column number must be either 0, 1, or 2.\n")
            return False
        
        if self.board.c[row][col] != " ":
            print("The cell is already taken.")
            print("Please make another selection.\n")

            return False
        return True
    
    # method to check if the board is full
    def checkFull(self):
        for row in self.board.c:
            if " " in row:
                return False
        return True
    
    # method to check winner
    def checkWin(self):
            # rows and columns
            for i in range(3):
                if all(self.board.c[i][j] == self.turn for j in range(3)):
                    return True
                if all(self.board.c[j][i] == self.turn for j in range(3)):
                    return True

            # diagonals
            if all(self.board.c[i][i] == self.turn for i in range(3)):
                return True
            if all(self.board.c[i][2 - i] == self.turn for i in range(3)):
                return True

            return False
    
    # this method checks if the game has ended or not
    def checkEnd(self):
        if self.checkWin():
            print(self.turn +" IS THE WINNER!!!")
            return True
        
        if self.checkFull():
            print("DRAW! NOBODY WINS!")
            self.board.printBoard()
            return True
        
        return False
   
   #Main game starting point
    def playGame(self):
        print("\nNew Game: X goes first.\n")
        self.board.printBoard()

        while True:
            print(self.turn + "'s turn.")
            print("Where do you want your " + self.turn + " placed?")
            print("Please enter row number and column number separated by a comma.")

            move = input()
            try:
                row,col = move.split(",")
                row= int(row)
                col= int(col)
                print("You have entered row #"+ str(row))
                print("\t   and column #"+str(col))

            except:
                print("Invalid input format. Try again.")
                continue
            
            if not self.validateEntry(row,col):
                continue
            
            self.board.c[row][col]= self.turn
            print("Thank you for your selection.")  
            self.board.printBoard()


            if self.checkEnd():
                break

            self.switchPlayer()



def main():
# first initializes a variable to repeat the game
    gameContinued = True

    while gameContinued:
        game = Game()
        game.playGame()

        again = input("Another game? Enter Y or y for yes.\n")
        if again.lower()!="y":
            gameContinued = False
    print("Thank you for playing!")
            

# call to main() function
if __name__ == "__main__":
    main()
