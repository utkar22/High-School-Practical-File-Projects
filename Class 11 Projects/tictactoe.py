def ttt():
    grid=[""," "," "," "," "," "," "," "," "," "]
    print ("Lets play Tic Tac Toe!")
    print ("Guide:")
    print (1,2,3,sep="|")
    print (4,5,6,sep="|")
    print (7,8,9,sep="|")
    print ("Begin!")
    for a in range(0,9):
        if a%2==0:
            b="X"
        else:
            b="O"
        print (grid[1],grid[2],grid[3],sep="|")
        print (grid[4],grid[5],grid[6],sep="|")
        print (grid[7],grid[8],grid[9],sep="|")
        while True:
            print ("Turn of",b)
            c=int(input())
            if grid[c].isspace()==True:
                grid[c]=b
                break
            else:
                print("Please enter in a correct spot")
        win=winah(grid,b)
        if win==1:
            print (b,"wins!!!")
            break
    else:
        print ("Its a draw!")

def winah(grid,b):
    if grid[1]==grid[2]==grid[3]==b or grid[4]==grid[5]==grid[6]==b or grid[7]==grid[8]==grid[9]==b or grid[1]==grid[4]==grid[7]==b or grid[2]==grid[5]==grid[8]==b or grid[3]==grid[6]==grid[9]==b or grid[1]==grid[5]==grid[9]==b or grid[3]==grid[5]==grid[7]==b:
        win=1
    else:
        win=0
    return (win)
            
            
        
    
