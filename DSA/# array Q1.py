# array Q1

arr=[]

for i in range(0,25):
    num=int(input("enter your number to be entered in the array:"))
    arr.append(num)

s=int(input("enter number to be searched:"))
c=0

for i in arr:
    if i==s:
        c=c+1

for i in arr:
    if i==s:
        print("element found")
        print("no. of times element appeared:",c)