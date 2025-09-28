#question 6

def find_dog():
    a=input("Enter a string to check for word dog: ")
    count = a.count("dog")
    if count>0:
        print("True")
        return True
    else:
        print("False")
        return False
    
find_dog()
    


