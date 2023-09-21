# question 8

def consonant_subseq():
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    in_str = input("Enter a string to find longest consonant subsequence: ")
    
    for char in in_str:
        if char in vowels:
            in_str = in_str.replace(char, "")
                
    out_list = in_str.split(" ")

    max = 0
    out_index = 0
    for i in range(0, len(out_list)):
        element = out_list[i]
        if len(element) > max:
            max = len(element)
            out_index = i
    
    print("Longest consonant sequence is:", out_list[out_index])

consonant_subseq()