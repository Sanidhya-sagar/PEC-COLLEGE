#question 7

def count_dog():
    string = input("Enter a sentence to count number of word dog has appeared:")
    count = string.count("dog")
    print("Found", count, "number of word dog.")

count_dog()