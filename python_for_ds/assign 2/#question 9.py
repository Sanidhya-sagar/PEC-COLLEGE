#question 9

def challan():
    speed = int(input("Enter speed: "))
    birthday_input = input("Is it your birthday(y/n): ")
    birthday = False
    if birthday_input =="y":
        birthday = True
    elif birthday_input =="n":
        birthday = False
    else:
        print("Invalid! Assuming no.")
    Challan = caught_speeding(speed, birthday)
    print(Challan)

def caught_speeding(speed = 0, birthday = False):
    no_range_high = 61
    small_range_high = 81
    if not birthday:
        if speed in range(no_range_high):
            return "No Challan"
        elif speed in range(no_range_high, small_range_high):
            return "Small Challan"
        elif speed >= small_range_high:
            return "Heavy Challan"
    elif birthday:
        if speed in range(no_range_high + 5):
            return "No Challan"
        elif speed in range(no_range_high + 5, small_range_high + 5):
            return "Small Challan"
        elif speed >= small_range_high + 5:
            return "Heavy Challan"
        
challan()