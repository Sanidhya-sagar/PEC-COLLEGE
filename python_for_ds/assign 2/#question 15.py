#question 15

print("series 2 +22 + 222 + 2222 + .. n terms")

terms=int(input("enter number of terms:"))
sum1=0
for i in range (1,terms + 1):
    sum1 += int('2' * i)

print("sum of the series:",sum1)