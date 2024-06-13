# question 6

number_of_students = int(input("Enter the number of students of ehich E-mail IDs need to entered: "))

email = list()
user_name = list()
domain_name = list()

for i in range(number_of_students):
    email.append(input("Enter the email ID: "))

for j in range (len(email)):
    temp_string = email[j]
    user_name_string = str()
    domain_name_string = str()
    count_user_name = 0
    count_domain_name =0
    for k in range (len(temp_string)):
        if temp_string[k] == "@":
            count_domain_name = (len(temp_string) - k) - 1
            break
        elif temp_string[k] != "@":
            count_user_name +=1

    user_name_string = temp_string[0:count_user_name]
    domain_name_string = temp_string[-count_domain_name:]

    user_name.append(user_name_string)
    domain_name.append(domain_name_string)

print(tuple(email))
print(tuple(user_name))
print(tuple(domain_name))