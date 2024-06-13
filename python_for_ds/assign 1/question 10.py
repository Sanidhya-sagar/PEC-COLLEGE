# question 10

a=int(input("enter your number:"))

i = 0
bnum = []
while a!=0:
    rem = a%2
    bnum.insert(i, rem)
    i = i+1
    a = int(a/2)

i = i-1
print("Binary Value is:")
while i>=0:
    print(end=str(bnum[i]))
    i = i-1
print()
