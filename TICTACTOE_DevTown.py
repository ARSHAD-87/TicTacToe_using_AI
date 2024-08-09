def ConstBoard(board):
    print("Current state of Board : \n\n")
    for i in range(9):
        if((i>0) & (i%3==0)):
            print("\n")
        if(board[i]==0):
            print("_ ",end=" ")
        if(board[i]==-1):
            print("X ",end=" ")
        if(board[i]==1):
            print("O ",end=" ")
            
def User1Turn(board):
    pos=int(input("\n\nEnter X's pos(1-9):"))
    if(board[pos-1]!=0):
        print("Wrong Move")
        exit(0)
    board[pos-1]=-1

def User2Turn(board):
    pos=int(input("\n\nEnter O's pos(1-9):"))
    if(board[pos-1]!=0):
        print("\n\nWrong Move")
        exit(0)
    board[pos-1]=1

def analyseboard(board):
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(8):
        if(board[cb[i][0]]!=0 and board[cb[i][0]]==board[cb[i][1]] and board[cb[i][1]]==board[cb[i][2]]):
            return board[cb[i][0]]
    return 0


def minmax(board, player):
    x= analyseboard(board)
    if(x!=0):
        return(x*player)    
    pos=-1
    value = -2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minmax(board, player*-1)
            board[i]=0   
            if(score>value):
                value=score
                pos=i  
    if(pos==-1):
        return 0
    return value            
                          
def CompTurn(board):
    pos=-1
    value = -2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minmax(board, -1)
            board[i]=0   
            if(score>value):
                value=score
                pos=i            
    board[pos]=1
           
def main():
    print("\n<---------------------------------------- Tic Tac Toe Game ---------------------------------------->")
    choice= int(input("Enter 1 for sngle Player \nEnter 2 for Multi-Player\nEnter Choice:"))
    board=[0,0,0,0,0,0,0,0,0]
    if (choice == 1):
        print("Computer: O vs You: X")
        player=int(input("Enter 1 to play 1(st) or 2 for 2(nd): "))
        for i in range(0,9):
            if(analyseboard(board)!=0):
                break  
            if((i+player)%2==0):
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)                      
    else:
        for i in range(9):
            if(analyseboard(board)!=0):
                break
            if(i%2==0):
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)
                
    ConstBoard(board)
    if(analyseboard(board)==0):
        print("\n\nDraw!")
    elif(analyseboard(board)==-1):
        print("\n\nPlayer 1 Wins!")
    else:
        print("\n\nPlayer 2 Wins!")
        
main()

