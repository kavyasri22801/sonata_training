num = int(input("enter a number"))
temp = num
pal = 0
while temp > 0:
    pal = (pal*10) + (temp %10);
    temp = temp//10
if pal == num:
    print("Palindrome \n")
else:
    print("Not Palindrome)