#question 5

def domain_name():
    email = input("enter your email for domain name:")
    res = email[email.index('@') + 1 : ]
    print("The extracted domain name : " + str(res))

domain_name()