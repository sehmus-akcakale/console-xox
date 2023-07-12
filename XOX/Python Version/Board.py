
class Board:
    
    def __init__(self):
        self.board = [[" " , " ", " "], [" " , " ", " "], [" " , " ", " "]]
        # 1 -- White // 2 -- Black
        self.currentPlayer = 1 
        self.moveCount = 0
       
       
       
    def isTie(self):
        # If total count is 9 and game don't end it means game is tie .
        return self.moveCount == 9
        
        
    
    def rowControl(self, row : int, column : int):
        symbol = self.board[row - 1][column - 1]
        for i in range(3):
            if(symbol != self.board[row - 1][i]):
                return False
        return True
    
    
    
    def columnControl(self ,row : int, column : int):
        symbol = self.board[row -1][column - 1]
        for i in range(3):
            if(symbol != self.board[i][column - 1]):
                return False        
        return True
    
    
    
    def diagonalControl(self,row : int, column : int):
        if(row == column):
            symbol = self.board[row - 1][column - 1]
            for i in range(3):
                if(symbol != self.board[i][i]):
                    return False
            return True
        else:
            return False
                
                
                
    def otherdiagonalControl(self,row : int, column : int):
        if(row + column == 4):
            symbol = self.board[row - 1][column - 1]
            i = 2 
            for j in range(3):
                if (symbol != self.board[i][j]):
                    return False
                i = i - 1 
            return True
        else:
            return False
                
                
                
    def isEnded(self):
        return self.isTie()
    
    
    
    def getCurrentPlayer(self):
        return self.currentPlayer
    
    
    
    def isValidMove(self,row : int , column : int) :
        if(row < 1 or row > 3 or column < 1 or column > 3):
            return False
        if(type(row) != int or type(column) != int):
            return False
        return True
    
    
    
    def getSymbol(self):
        symbol = " "
        if (self.getCurrentPlayer() == 1):
            symbol = "X"
        else:
            symbol = "O"
        return symbol
    
    

    def getLocation(self, row : int , column : int):
        return self.board[row - 1][column - 1]
    
    
    
    def setLocation(self, row : int , column : int , symbol : str):
        self.board[row - 1][column - 1] = symbol
        
        
        
    def move(self,row : int , column : int):
        self.board[row-1][column - 1] = self.getSymbol()
        self.currentPlayer = 3 - self.getCurrentPlayer()
        self.moveCount = self.moveCount + 1 
    
    
    
    def __str__(self) :
        string = "    1   2   3\n" + "   -----------\n"
        for row in range(3):
            string += str(row + 1) + " "
            for col in range(3):
                string += "|" + " " + self.board[row][col] + " "
                if col == 2:
                    string += "|"
            string += "\n" + "   -----------\n"
        return string

