import os
import sys

def main():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    steps = 9
    start = 1
    choice = 0


    def drawBoard(choice,mark):

        board[choice]= mark
        
        print(" %c | %c | %c " %(board[1],board[2],board[3]))
        print("-----------")
        print(" %c | %c | %c " %(board[4],board[5],board[6]))
        print("-----------")
        print(" %c | %c | %c " %(board[7],board[8],board[9]))
        print("-----------")

    def getInputs(player,choice,mark):
        player,choice,mark = player,choice,mark
        print(f"Player {player} chance")
        choice = int(input("Enter the position between [1-9] where you want to mark : "))
        if board[choice] == ' ':
            if 0< choice <10:
                drawBoard(choice,mark)
                
            else:
                print("Player {} chance".format(player))
                print("Enter a Valid position")
                getInputs(player,choice,mark)
        else:
            print("Your position is already entered")
            getInputs(player,choice,mark)
        return choice

    def gameCheck(player):
        #Horizontal winning condition    
        if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
            gameReplay(player)   
        elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
            gameReplay(player)    
        elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
            gameReplay(player)   
        #Vertical Winning Condition    
        elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
            gameReplay(player)    
        elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
            gameReplay(player)    
        elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
            gameReplay(player)    
        #Diagonal Winning Condition    
        elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
            gameReplay(player)    
        elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
            gameReplay(player)    
        #Match Tie or Draw Condition    
        elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
            gameDraw()

            

    def gameReplay(player):
        print("Player {} has won the game".format(player))
        replay = input("Do you want to play again? (Y/N)")
        if replay == 'Y' or replay =='y':
            main()

        elif replay == 'N' or replay =='n':
            print("Thank You")
        
        

    def gameDraw():
        print("Game Draw")
        gameReplay(player)


    drawBoard(0,' ')

    while True:
        
        os.system('cls')
        if (start %2 ==1):
            player =1
            mark = 'X'
            choice = getInputs(player,choice,mark)
            gameCheck(player)
            
        elif(start%2 == 0):
            player =2
            mark = 'O'
            choice = getInputs(player,choice,mark)
            gameCheck(player)
        
        start = start +1
        os.system('cls')

main()
