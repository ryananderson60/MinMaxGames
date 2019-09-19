#Make board:
import random
import sys

output = open("Output.txt", "w")

class Pentago:
    """
    A class for the turn based game Pentago.
    Author: Ryan Anderson
    Date: 8-1-19
    """
    #Constructor method for Pentago game. Sets Andy's color.
    #
    #Params:
    #   humanPlayerName: human player name
    #   humanPlayerColor: desired color for human player
    def __init__(self, humanPlayerName, humanPlayerColor):
        self.board = [["." for x in range(6)] for y in range(6)]
        self.humanPlayer = (humanPlayerName, humanPlayerColor.lower())
        self.andy = ("Andy", self.getAndyColor())
        self.player1, self.player2 = Pentago.setRandomPlayers(self.humanPlayer,
                                                              self.andy)
        self.nextMove = self.player1
        self.movesMade = []
        
    def setRandomPlayers(player1, player2):
        num = random.randint(1,10)
        if num <= 5:
            return player1, player2
        else:
            return player2, player1
    
    def getAndyColor(self):
        if self.humanPlayer[1] == "w" or self.humanPlayer[1] == "W":
            return "b"
        else:
            return "w"
            
    def displayBoardPretty(self):
        middle = 0
        print("-" * 17)
        for i in self.board:
            divider = 0
            print("|", end = " ")
            for t in i:
                if divider == 3:
                    print("|", end=" ")
                print(t, end=" ")
                divider += 1
            middle += 1
            if middle == 3:
                print("|")
                print("-" * 17)
                continue
            print("|")
        print("-" * 17)

    def displayBoard(self):
        for i in self.board:
            for t in i:
                print(t, end="")
            print("")

    def boardConfig(self):
        message = "Player 1 Name (player who moves first) {:>10}\n".format(\
            (self.player1[0]))
        message += "Player 2 Name {:>35}\n".format(self.player2[0])
        message += "Player 1 Token Color (B or W) {:>16}\n".format(\
            (self.player1[1]))
        message += "Player 2 Token Color (B or W) {:>16}\n".format(\
            (self.player2[1]))
        message += "Player to Move Next (1 or 2) {:>20}\n".format(\
            (self.nextMove[0]))
        rows = self.getRows()
        message += "Next 6 lines: board state {:>25}\n".format(\
            (rows[0]))
        message += "Remaining lines: list of moves made, {:>14}\n".format(\
                   (rows[1]))
        message += "in order from first to last, {:>22}\n".format(\
                   (rows[2]))
        message += "alternating players. {:>30}\n".format(\
            (rows[3]))
        message += "{:>51}\n".format(rows[4])
        message += "{:>51}\n".format(rows[5])
        for i in self.movesMade:
            message += "{:>51}\n".format(" ".join(i).upper())
        output.write(message)
        print(message)
        
    def getRows(self):
        rows = []
        for i in self.board:
            s = ""
            for t in i:
                s += t
            rows.append(s)
        return rows

    def getHumanMove(self):
        keepGoing = True
        while(keepGoing):
            move = input("Enter next move or q to quit: ")
            if move == "q":
                sys.exit()
            move = move.split(" ")
            if (len(move[0]) != 3):
                print("invalid amount of placement string length")
                continue
            if (move[0][0] != "1" and move[0][0] != "2"
                and move[0][0] != "3" and move[0][0] != "4"):
                print("invalid placement input")
                continue
            if("1" > move[0][2] or "9" < move[0][2]):
                print("invalid placement input")
                continue
            if len(move) != 2:
                print("invalid amount of move length")
                continue
            if (len(move[1]) != 2):
                print("invalid rotate input")
                continue
            if (move[1][0] != "1" and move[1][0] != "2"
                and move[1][0] != "3" and move[1][0] != "4"):
                print("invalid rotate input")
                continue
            if (move[1][1] != "r" and move[1][1] != "R"
                and move[1][1] != "l" and move[1][1] != "L"):
                print("invalid rotate input")
                continue

            #check letterMove can be placed
            if (self.checkPlacement(move[0][0] + "/" + move[0][2])):
                return move
            else:
                print("invalid placement: cell taken")
                continue

    def getAndyMove(self):
        keepGoing = True
        while(keepGoing):
            placementBlock = str(random.randint(1, 4))
            placementSquare = str(random.randint(1,9))
            move = placementBlock + "/" + placementSquare
            if (self.checkPlacement(move) == False):
                continue
            rotateBlock = str(4)
            rotateDirection = "L"
            move += " "
            move += rotateBlock
            move += rotateDirection
            move = move.split(" ")
            return move
            
    def checkPlacement(self, placement):
        square = self.getSquare(placement[0])
        placementCell = placement[2]
        if square[int(placementCell) - 1] == ".":
            return True
        else:
            return False

    def placeMove(self, move):
        blockNumber = move[0]
        placement = int(move[2]) - 1
        square = self.getSquare(blockNumber)
        square[placement] = self.nextMove[1]
        self.copyContents(blockNumber, square)

    def copyContents(self, blockNumber, square):
        if blockNumber == "1":
            self.board[0][0:3] = square[0:3]
            self.board[1][0:3] = square[3:6]
            self.board[2][0:3] = square[6:]
        elif blockNumber == "2":
            self.board[0][3:6] = square[0:3]
            self.board[1][3:6] = square[3:6]
            self.board[2][3:6] = square[6:]
        elif blockNumber == "3":
            self.board[3][0:3] = square[0:3]
            self.board[4][0:3] = square[3:6]
            self.board[5][0:3] = square[6:]
        else:
            self.board[3][3:6] = square[0:3]
            self.board[4][3:6] = square[3:6]
            self.board[5][3:6] = square[6:]

    def getSquare(self, squareNumber):
        square = []
        if squareNumber == "1":
            square.extend(self.board[0][0:3])
            square.extend(self.board[1][0:3])
            square.extend(self.board[2][0:3])
        elif squareNumber == "2":
            square.extend(self.board[0][3:6])
            square.extend(self.board[1][3:6])
            square.extend(self.board[2][3:6])
        elif squareNumber == "3":
            square.extend(self.board[3][0:3])
            square.extend(self.board[4][0:3])
            square.extend(self.board[5][0:3])
        else:
            square.extend(self.board[3][3:6])
            square.extend(self.board[4][3:6])
            square.extend(self.board[5][3:6])
        return square

    def checkGameWinner(self):
        winners = set()
        winner = False
        for row in range(len(self.board)):
            for column in range(6):
                winner = self.checkDiagonalDown(row, column)
                if (winner != False):
                    winners.add(winner)
                winner = self.checkDiagonalUp(row, column)
                if (winner != False):
                    winners.add(winner)
                winner = self.checkUpDown(row, column)
                if (winner != False):
                    winners.add(winner)
                winner = self.checkLeftRight(row, column)
                if (winner != False):
                    winners.add(winner)

        if len(winners) == 0:
            return False
        else:
            return winners
        
    def checkDiagonalDown(self, startRow, startColumn):
        count = 1
        if self.board[startRow][startColumn] == ".":
            return False
        letter = self.board[startRow][startColumn].lower()
        currentRow = startRow - 1
        currentColumn = startColumn - 1
        #check up and left
        while(currentRow >= 0 and currentColumn >= 0):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow -= 1
                currentColumn -= 1
            else:
                break
        currentRow = startRow + 1
        currentColumn = startColumn + 1
        #check down and right
        while(currentRow <= 5 and currentColumn <= 5):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow += 1
                currentColumn += 1
            else:
                break

        if count < 5:
            return False
        else:
            return letter

    def checkDiagonalUp(self, startRow, startColumn):
        count = 1
        if self.board[startRow][startColumn] == ".":
            return False
        letter = self.board[startRow][startColumn].lower()
        currentRow = startRow - 1
        currentColumn = startColumn + 1
        #check up and right
        while(currentRow >= 0 and currentColumn <= 5):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow -= 1
                currentColumn += 1
            else:
                break
        currentRow = startRow + 1
        currentColumn = startColumn - 1
        #check down and left
        while(currentRow <= 5 and currentColumn >= 0):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow += 1
                currentColumn -= 1
            else:
                break

        if count < 5:
            return False
        else:
            return letter

    def checkUpDown(self, startRow, startColumn):
        count = 1
        if self.board[startRow][startColumn] == ".":
            return False
        currentRow = startRow - 1
        currentColumn = startColumn
        letter = self.board[startRow][startColumn].lower()
        #check up
        while(currentRow >= 0):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow -= 1
            else:
                break
        currentRow = startRow + 1
        #check down
        while(currentRow <= 5):
            if self.board[currentRow][currentColumn] == letter:
                count += 1
                currentRow += 1
            else:
                break

        if count < 5:
            return False
        else:
            return letter

    def checkLeftRight(self, startRow, startColumn):
         count = 1
         if self.board[startRow][startColumn] == ".":
            return False
         letter = self.board[startRow][startColumn].lower()
         currentRow = startRow
         currentColumn = startColumn - 1
         #check left
         while(currentColumn >= 0):
             if self.board[currentRow][currentColumn] == letter:
                 count += 1
                 currentColumn -= 1
             else:
                 break
         currentColumn = startColumn + 1
         #check right
         while(currentColumn <= 5):
             if self.board[currentRow][currentColumn] == letter:
                 count += 1
                 currentColumn += 1
             else:
                 break

         if count < 5:
             return False
         else:
             return letter

    def setNextMove(self):
        if self.nextMove == self.player1:
            self.nextMove = self.player2
        else:
            self.nextMove = self.player1

    def rotateMove(self, move):
        squareNumber = move[0]
        direction = move[1]
        square = self.getSquare(squareNumber)
        newSquare = []
        if direction == "L" or direction == "l":
            newSquare.append(square[2])
            newSquare.append(square[5])
            newSquare.append(square[8])
            newSquare.append(square[1])
            newSquare.append(square[4])
            newSquare.append(square[7])
            newSquare.append(square[0])
            newSquare.append(square[3])
            newSquare.append(square[6])
        else:
            newSquare.append(square[6])
            newSquare.append(square[3])
            newSquare.append(square[0])
            newSquare.append(square[7])
            newSquare.append(square[4])
            newSquare.append(square[1])
            newSquare.append(square[8])
            newSquare.append(square[5])
            newSquare.append(square[2])
            
        self.copyContents(squareNumber, newSquare)
            
def printWelcome():
    message = "Welcome to Pentago!\n"
    message += "You will play against an AI named Andy\n"
    message += "Have fun and good luck!\n"
    message += ("-" * 40) + "\n"
    print(message, end = "")
    output.write(message)
    
def main():
    keepGoing = True
    printWelcome()
    beginMessage = "The game will now begin!\n\n"
    while(1):
        humanName = input("Please enter your name: ")
        if humanName == "Andy":
            print("Name can not be 'andy'")
            continue
        break
    humanColor = input("Please enter your desired color ('w' or 'b'): ")
    print(beginMessage, end = "")
    output.write(beginMessage)
    game = Pentago(humanName, humanColor)
    count = 1
    while(count < 36):
        game.boardConfig()
        if game.nextMove[0] == "Andy":
            move = game.getAndyMove()
        else:
            move = game.getHumanMove()
        game.placeMove(move[0])
        winners = game.checkGameWinner()
        if(winners):
            print("Winner: {}!".format(winners))
            game.displayBoardPretty()
            sys.exit()
        game.rotateMove(move[1])
        winners = game.checkGameWinner()
        if(winners):
            print("Winners: {}!".format(winners))
            game.displayBoardPretty()
            sys.exit()
        game.movesMade.append(move)
        game.setNextMove()
        count += 1
    output.close()
        
if __name__ == "__main__":
    main()

##testGame = Pentago("james", "w")
##testGame.board[0][0] = "w"
##testGame.board[1][0] = "w"
##testGame.board[2][0] = "w"
##testGame.board[3][0] = "w"
##testGame.board[4][0] = "w"
##r = testGame.checkGameWinner()
##print(r)
