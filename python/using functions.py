# palindrome using function
def palin(n):
    temp = n
    pal = 0
    while n > 0:
        pal = (pal*10) + n %10;
        n=n//10
    if (temp == pal):
        print(" palindrome")
    else:
        print(" not a palindrome")
r=int(input("enter a number"))
result=palin(r)


# count words in a sentence using function
def count(s):
    k=s.split()
    return len(k)
r=input("enter a string")
a=count(r)
print(a)

#largest number among three numbes using fucntion
def larger(n1,n2,n3):
    if ((n1 > n2) and (n1 > n3)):
        return n1
    elif (n2 > n3):
        return n2
    else:
        return n3
result=larger(10,40,20)
print(result)


#rock, paper , scissor game using function
def game(p1,p2):
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
p1=input("player1 turn")
p2=input("player2 turn")
s=game(p1,p2)
print(s)

#simple interest using function
def si(p,t,r):
    i = (p * t * r) / 100
    return i
a=si(47500,10,5)
print(a)


#fing age using fucntion
def age(n):
    c=100-(n)
    return c
n=int(input("enter your age"))
d=age(n)
print(d,'te reach century')