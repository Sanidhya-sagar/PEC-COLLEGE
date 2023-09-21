# question 2

l1 = list()
l2 = list()

length_1 = int(input("Enter length of list 1 : "))

for i in range (length_1):
    l1.append(int(input("Enter element: ")))

length_2 = int(input("Enter length of list 1 : "))

for j in range(length_2):
    l2.append(int(input("Enter the element: ")))

l1 += l2

print(l1)