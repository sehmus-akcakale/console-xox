from Board import Board


def main():
    
    board = Board()
    print(board)
    
    while(not board.isEnded()):
        
        row = int(input("Player " + str(board.currentPlayer) + " enter row :"))
        column = int(input("Player " + str(board.currentPlayer) + " enter column :"))
        
        if (not board.isValidMove(row, column)):
            print("Please try again !!!")
            
        else:
            
            if(board.getLocation(row,column) != " "):
                print("It is not a valid location !!!")
                
            else:
                
                board.move(row,column)
                win = board.rowControl(row,column) or board.columnControl(row,column) or board.diagonalControl(row,column) or board.otherdiagonalControl(row,column)
                print(board)
                
                if(win):
                    print(board)
                    print("Player " + str(3 - board.getCurrentPlayer()) + " has won the game !!!")
                    break
                
    if(board.isTie()):
        print("No one won the game !!!")
                

if __name__ == "__main__":
    main()