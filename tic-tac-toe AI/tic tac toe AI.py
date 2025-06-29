
def Playboard(board):
    print("Current State Of Board : \n\n")
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):    
            print("X ",end=" ")
    print("\n\n")

def PlayerTurn(board):
    position=input("Enter X's position from [1---9]: ")
    position=int(position)
    if(board[position-1]!=0):
        print("Wrong Move!!!")
        exit(0)
    board[position-1]=-1




def minimax(board,player):
    x=analyzeboard(board)
    if(x!=0):
        return (x*player)
    position=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minimax(board,(player*-1));
            if(score>value):
                value=score
                position=i
            board[i]=0

    if(position==-1):
        return 0
    return value



def CompTurn(board):
    position=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board, -1)
            board[i]=0
            if(score>value):
                value=score
                position=i
 
    board[position]=1



def analyzeboard(board):
    combinations =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in range(0,8):
        if(board[combinations[i][0]] != 0 and
           board[combinations[i][0]] == board[combinations[i][1]] and
           board[combinations[i][0]] == board[combinations[i][2]]):
            return board[combinations[i][2]]
    return 0



def main():


    board=[0,0,0,0,0,0,0,0,0]

    print("Computer : O Vs. You : X")
    player= input("Enter to play 1(st) or 2(nd) :")
    player = int(player)
    for i in range (0,9):
        if(analyzeboard(board)!=0):
            break
        if((i+player)%2==0):
            CompTurn(board)
        else:
            Playboard(board)
            PlayerTurn(board)
         

    x= analyzeboard(board)
    if(x==0):
         Playboard(board)
         print("Draw! No one Wins !!")
    if(x==-1):
         Playboard(board)
         print("You Wins!! AI Loose !!")
    if(x==1):
         Playboard(board)
         print("You Loose ! AI Wins !!!")
       


main()