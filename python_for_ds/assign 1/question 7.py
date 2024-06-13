# question 7

string_1 = str(input("Enter a sentence: \n"))

count_alpha = 0
count_digit = 0
count_symbol = 0
count_upper_case = 0
count_lower_case = 0

string_2 = str()

length = len(string_1)

for i in range(0,length):
    if string_1[i].isalpha():
        count_alpha += 1
        string_2 += string_1[i]
    elif string_1[i].isdigit():
        count_digit +=1
    elif not(string_1[i].isalnum()):
        count_symbol +=1

for j in range(0,len(string_2)):
    if (string_2[j].isupper()):
        count_upper_case +=1
    elif (string_2[j].islower()):
        count_lower_case +=1

print("Number of alphabets:",count_alpha)
print("Number of digits:",count_digit)
print("Number of symbols:",count_symbol)
print("Number of upper case aplhabets:",count_upper_case)
print("Number of lower case alphabets:",count_lower_case)