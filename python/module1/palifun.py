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