# question 9

print("Condition for setting up password:")
print("01. Password must be at least 5 letters long.")
print("02. It must contain  \" & \" symbol.")
print("03. It must contain atleast one uppercase and one lowercase alphabet. ")

password = str(input("Enter the PASSWORD: \n"))
count_upper = 0
count_lower = 0
count_symbol = 0

for i in range(0,len(password)):
    if (password[i].isupper()):
        count_upper += 1
    elif (password[i].islower()):
        count_lower += 1
    elif (password[i] == "&"):
        count_symbol += 1

if (len(password) >=5) and (count_lower >=1) and (count_upper >=1) and (count_symbol >=1):
    print("CORRECT PASSWORD ENETRED")
else:
    print("INCORRECT PASSWORD")
    