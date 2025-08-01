# Python Strings

# 1. Creating Strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''This is a
multi-line string'''

print(single_quote)
print(double_quote)
print(triple_quote)

# 2. String Concatenation
greeting = single_quote + ' ' + double_quote
print(greeting)

# 3. String Length
length = len(greeting)
print("Length:", length)

# 4. Accessing Characters (Indexing)
first_char = greeting[0]
last_char = greeting[-1]
print("First character:", first_char)
print("Last character:", last_char)

# 5. Slicing Strings
slice1 = greeting[0:5]   # 'Hello'
slice2 = greeting[6:]    # 'World'
print("Slice1:", slice1)
print("Slice2:", slice2)

# 6. String Methods
upper = greeting.upper()
lower = greeting.lower()
title = greeting.title()
replace = greeting.replace('World', 'Python')
split = greeting.split(' ')
print("Upper:", upper)
print("Lower:", lower)
print("Title:", title)
print("Replace:", replace)
print("Split:", split)

# 7. Stripping Whitespace
messy = "   Hello World!   "
clean = messy.strip()
print("Stripped:", clean)

# 8. Checking Substrings
contains = 'Hello' in greeting
print("Contains 'Hello':", contains)

# 9. Formatting Strings
name = "Alice"
age = 30
formatted1 = "My name is {} and I am {} years old.".format(name, age)
formatted2 = f"My name is {name} and I am {age} years old."
print(formatted1)
print(formatted2)

# 10. Escaping Characters
escaped = "He said, \"Python is awesome!\""
print(escaped)

# 11. Useful String Methods
print("Count of 'l':", greeting.count('l'))
print("Starts with 'Hello':", greeting.startswith('Hello'))
print("Ends with 'World':", greeting.endswith('World'))

# 12. Iterating Over a String
for char in greeting:
    print(char)

# 13. Joining Strings
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)
print(sentence)


