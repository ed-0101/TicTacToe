from os import system
from random import choice
import time
# This function Prints The Board
def print_board(board):
    
    """
        This Method Will Print The Board
        For The Tic Tac Toi Game
    """

    system('cls')
    print("\n","__"*50,sep="\n")
    print("__"*50,"\n")
    c = 1
    for z in range(3):
        if z==0:
            print(" "*30,end="\t")
            print("-"*25)
        else:
            print(" "*30,end="\t")
            print("-"*8,"-"*7,"-"*8,sep="+")
        for j in range(3):
            print(" "*30,end="\t")
            for i in range(3):
                if j==1:
                    print("|",f"{board[c]}".center(6," "),end="")
                    c += 1
                else:
                    print("|"," ".center(6," "),end="")

            print("|")
    print(" "*30,end="\t")
    print("-"*25)
    print("__"*50,"\n")
    
# This Function checks the winner conditions
def check_win(p,b1,s):
    r = False
    if b1[1] == b1[2] == b1[3] == s or b1[4] == b1[5] == b1[6] == s or b1[7] == b1[8] == b1[9] == s:
        r = True
    elif b1[1] == b1[4] == b1[7] == s or b1[2] == b1[5] == b1[8] == s or b1[3] == b1[6] == b1[9] == s:
        r = True
    elif b1[1] == b1[5] == b1[9] == s or b1[3] == b1[5] == b1[7] == s:
        r = True
    if r:
        print(f"{p}, Won The Game...".center(30," "),"\n")
    else:
        pass
    return r
    

# This function takes choice from Player and also Track the empty places
def move(es,p,s,bd):
    while True:
        print("\n    Available Places    : ",es)
        print("")
        if p == "Computer":
            n = choice(es)
            print(f"{p}\'s choice is : {n}")
        else:
            n = int(valid_in(f"{p}, Enter Place"))
        if n not in es:
            print("Invalid Choice!! Try Agian...".center(30," "),"\n")
            continue
        elif str(n) == '':
            print("Blank Input !! Try Agian... ".center(30," "),"\n")
            continue
        else:
            board1[n] = s  
            es.remove(n)
            print_board(board1)
            return check_win(p,bd,s)
            break
    
#  This function give alternative chance to Players
def user_move(es,p1,p2,bd):
        for i in range(9): 
            if i%2 == 0:
                if move(es,p1,"X",bd):
                    msg = f"{p1}, Won The Game with {p2}"
                    __log(msg)
                    break
            else:
                if move(es,p2,"O",bd):
                    msg = f"{p2}, Won The Game with {p1}"
                    __log(msg)
                    break
        else:
            msg = f"It's a Tai !! Between {p1} and {p2}"
            print("It's a Tai !! You can play agian...".center(30," "),"\n")
            __log(msg)
            
#Valid Input Taker
def valid_in(st,ty=str):
    while True:
        print("")
        try:
            s = ty(input(f"{st} : ".center(30," ")))
            if s:
                #Emergency Exit Input  
                if s == 7230 or s == '7230':
                    system('cls')
                    print("\n\n","Emergency Exit...".center(100," "),"\n\n")
                    exit()
                else:
                    return s
                    break
            else:
                print("\n","Blank Input!!","Try Agian...".center(60," "))
        except Exception:
            print("\n","You entered an invalid value...".center(60," "))

#Log File
def __log(msg):
        with open('GameHistory.log', 'a') as f:
            tm = time.ctime()
            msg = "\t"+tm+'\t'+msg+"\n"
            f.write(msg)
            f.close()

#Game initialization        
opt = 1
while opt:
    b=[i for i in range(10)]
    print_board(b)
    input("Press Enter to Continue.... ".center(40," "))
    print("\n")
    board1=[" " for i in range(10)]
    print_board(board1)
    print("""
    Choose Any Option                    _____   __    
                                        / __    _ \ /  \  __
    1. With Computer                    |/   /   /   \/ \_/ / _/ 
                                            /   /       _ / /
    2. With Human                          /   /       /  / | |__/|
                                           \_/       //   \_/
    3. Game History

    4. Exit

    """)  
    while True:
        ch = valid_in("Choice",int)
        if ch == 1:
            p1 = "Computer"
            print("\n","You Are Playing With Computer".center(80," "))
            p2 = valid_in("Enter Your Name")
            if p1==p2:
                print("\n","Player Already Exist !!","Use Different Name",sep="\t")
                p2 = valid_in("Enter Your Name")
            break
        elif ch == 2:
            p1 = valid_in("Enter Player 1 Name")
            p2 = valid_in("Enter Player 2 Name")
            if p1==p2:
                print("\n","Player Already Exist !!","Use Different Name",sep="\t")
                p2 = valid_in("Enter Player 2 Name")
            break
        elif ch == 3:
            print("")
            with open('GameHistory.log', 'r') as f:
                print(f.read())
                f.close()
                ch = valid_in("To Reset Game History Press 1 ",int)
                if ch == 1:
                    open('GameHistory.log','w').close()
                else:
                    pass
            print("")
            continue
        elif ch == 4:
            system('cls')
            exit()
        else:
            print("\n","Invalid Choice !! Try Agian...".center(40," "))
    es = [i for i in range(1,10)]
    user_move(es,p1,p2,board1)
    print("__"*50,"\n")
    opt = int(valid_in("Want to Play Agian... Press 1  "))
    print("__"*50)
else:
    pass