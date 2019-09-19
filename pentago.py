#Make board:
import random

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
        self.humanPlayer = (humanPlayerName, humanPlayerColor.upper())
        self.andy = ("Andy", Pentago.getAndyColor(self.humanPlayer[1]))
        self.player1, self.player2 = Pentago.setRandomPlayers(self.humanPlayer,
                                                              self.andy)
        self.nextMove = "1"
        self.movesMade = []
        
    def setRandomPlayers(player1, player2):
        num = random.randint(1,11)
        if num <= 5:
            return player1, player2
        else:
            return player2, player1
    
    def getAndyColor(color):
        if color == "w" or "W":
            return "B"
        else:
            return "W"
            
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
        message += "Player to Move Next (1 or 2) {:>17}\n".format(\
            (self.nextMove))
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
            message += "{}\n".format(i)
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
    humanName = input("Please enter your name: ")
    humanColor = input("Please enter your desired color ('w' or 'b'): ")
    print(beginMessage, end = "")
    output.write(beginMessage)
    game = Pentago(humanName, humanColor)
    while(keepGoing):
        game.boardConfig()
        humanMove = input("Enter next move or q to quit: ")   
        if humanMove == "q":
            keepGoing = False
    output.close()
        
if __name__ == "__main__":
    main()
