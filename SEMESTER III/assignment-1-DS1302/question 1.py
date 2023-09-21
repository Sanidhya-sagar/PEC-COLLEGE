# question 1

print("enter your numbers for results:")
a=int(input("enter marks in maths:"))
b=int(input("enter marks in physics:"))
c=int(input("enter marks in chemistry:"))

avg=(a+b+c)/3
if avg>=40:
    print("pass")
else:
    print("fail")    