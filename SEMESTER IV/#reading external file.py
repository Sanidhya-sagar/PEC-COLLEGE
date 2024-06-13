#reading external file

def count_characters(filename):
    char_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                char_counts[char] = char_counts.get(char, 0) + 1
                
    return char_counts


filename = "F:\\vs code folder\\sem 4\\extfile.txt"  
char_counts = count_characters(filename)

for char, count in char_counts.items():
    print(f"{char}: {count}")


# for vowels
    


