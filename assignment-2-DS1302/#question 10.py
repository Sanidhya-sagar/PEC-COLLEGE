#question 10

list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]
answer = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        answer.append(list1[i] + list2[i])
print(answer)