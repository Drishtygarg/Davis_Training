# This program counts number of vowels in a string

# Take input string
s = input("Enter string: ")

count = 0   # counter for vowels

# Loop through each character
for ch in s:
    if ch.lower() in "aeiou":   # check if character is vowel
        count += 1

# Print result
print(count)

# Output:
# Enter string: hello
# 2