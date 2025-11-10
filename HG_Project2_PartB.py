
''' Hi, My name is Hitika Ghanani and below is the updated code for 'TIC TAC TOE'. 
I have build this game as a part of programming project. This is the improvised version where I applied Object Oreiented Programming using classes and objects and also implemented Minimax algorithm for computer player logic. So, now game has new mode - single player to play against computer
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
    def __init__(self, mode="multiplayer"):
        self.board = Board()
        self.turn = 'X'
        self.mode = mode
        self.humanPlayer = 'X'
        self.computerPlayer = 'O'
            
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
    
    # method to check winner for specific player using minimax
    def checkWinForPlayer(self, player):
        # rows and columns
            for i in range(3):
                if all(self.board.c[i][j] == player for j in range(3)) \
                or all(self.board.c[j][i] == player for j in range(3)):
                    return True

            # diagonals
            if all(self.board.c[i][i] == player for i in range(3)) \
            or all(self.board.c[i][2 - i] == player for i in range(3)):
                return True

            return False
    
    # minimax algorithm for finding best move of computer player
    def minimax(self, isMaximizing):
        if self.checkWinForPlayer(self.computerPlayer):
            return 10
        
        if self.checkWinForPlayer(self.humanPlayer):
            return -10
        
        if self.checkFull():
            return 0
        
        if isMaximizing:
            bestScore = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board.c[i][j] == " ":
                        self.board.c[i][j] = self.computerPlayer
                        score = self.minimax(False)
                        self.board.c[i][j] = " "
                        if score > bestScore:
                            bestScore = score
            return bestScore
        
        else:
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board.c[i][j] == " ":
                        self.board.c[i][j] = self.humanPlayer
                        score = self.minimax(True)
                        self.board.c[i][j] = " "
                        if score < bestScore:
                            bestScore = score
            return bestScore
        
    
    #method to find the best possible move for computer
    def bestMove(self):
        bestScore = float('-inf')
        bestMove = None

        for i in range(3):
                for j in range(3):
                    if self.board.c[i][j] == " ":
                        self.board.c[i][j] = self.computerPlayer
                        score = self.minimax(False)
                        self.board.c[i][j] = " "

                        if score > bestScore:
                            bestScore = score
                            bestMove = (i,j)

        return bestMove


            
   #Main game starting point
    def playGame(self):
        print("\nNew Game: X goes first.\n")
        self.board.printBoard()

        while True:
            #computer's turn
            if self.mode == "singleplayer" and self.turn == self.computerPlayer:
                print("Computer's turn O")
                move = self.bestMove()
                if move:
                    row,col = move
                    self.board.c[row][col] = self.turn
                    print("Computer have placed row #"+ str(row))
                    print("\t   and column #"+str(col))
                    self.board.printBoard()

                    if self.checkEnd():
                        break

                    self.switchPlayer()
                continue
            
            #human player turn
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
        print("\nChoose game mode:")
        print("1.Multiplayer(human vs human) \n2.Singleplayer(human vs computer)")
        modeChosen = input("Enter option 1 or 2\n")

        if modeChosen == '2':
            game = Game(mode="singleplayer")
        else:
            game = Game(mode="multiplayer")

        game.playGame()

        again = input("Another game? Enter Y or y for yes.\n")
        if again.lower()!="y":
            gameContinued = False
    print("Thank you for playing!")
            

# call to main() function
if __name__ == "__main__":
    main()
