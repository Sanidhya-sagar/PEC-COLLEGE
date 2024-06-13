# String manipulation examples

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation Result:", result)

# String Formatting
name = "John"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print("Formatted Message:", message)

# Substring
sentence = "This is a sample sentence."
substring = sentence[5:10]
print("Substring:", substring)

# String Length
text = "Python is fun!"
length = len(text)
print("Length of the string:", length)

# Uppercase and Lowercase
text = "Hello World"
upper_text = text.upper()
lower_text = text.lower()
print("Uppercase:", upper_text)
print("Lowercase:", lower_text)

# Replace
sentence = "I like cats."
new_sentence = sentence.replace("cats", "dogs")
print("Replaced Sentence:", new_sentence)

# Split
sentence = "Python is awesome"
words = sentence.split()
print("Split Words:", words)

# Join
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined Sentence:", sentence)

# Strip Whitespace
text = "   Hello   "
stripped_text = text.strip()
print("Stripped Text:", stripped_text)