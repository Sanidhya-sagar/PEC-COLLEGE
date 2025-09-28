# question 4

list_1 = list()

option_4 = "y"
while (option_4 == "y"):

    print("Choose the following options: ")
    print("1. Press 1 to insertion of elements in the list." )
    print("2. Press 2 to deletion of elements from the list.")

    option = int(input(":"))

    if (option == 1):
        option_2 = "y"
        while (option_2 == 'y'):
            index_no = int(input("Enter the index number: "))
            element  = int(input("Enter the element: "))
            list_1.insert(index_no,element)
            print("Press 'y' to continue or 'n' to finish. ")
            option_2 = input(":")
        print(list_1)
    
    elif (option == 2):
        print("Choose the following options: ")
        print("1. press 1 to delete item by its value.")
        print("2. press 2 to delete item by its index number.")
        print("3. Press 3 to slice the items from the list.")

        option_3 = int(input(":"))

        if (option_3 == 1):
            list_1.remove(int(input("Enter Element to deleted: ")))
            
        elif (option_3 == 2):
            list_1.pop(int(input("Enter the Index Number: ")))
            
        elif (option_3 == 3):
            del list_1[int(input("Enter the initial index no.: ")):int(input("Enter the final index no.: "))]
            

    
    option_4 = input("Press 'y' to delete elements or 'n' to finish.")
    print(list_1)