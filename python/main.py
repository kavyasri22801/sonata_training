n=0
while(n>0):
    a=int(input("choose yes or no")
    p1=input("player1 turn")
    p2=input("player2 turn")
    if(p1=="rock" and p2=="scissor"):
        print("p1 win")
    elif(p1=="scissor" and p2=="rock"):
        print("p2 win")
    elif(p1=="rock" and p2=="paper"):
        print("p2 win")
    elif(p1=="paper" and p2=="rock"):
        print("p1 win")
    elif(p1=="scissor" and p2=="paper"):
        print("p1 win")
    elif(p1=="paper" and p2=="scissor"):
        print("p2 win")
    else:
        print("clash")