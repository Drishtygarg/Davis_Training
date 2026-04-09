# This program counts occurrences of a character

# Take input
s = input("Enter string: ")
ch = input("Enter character to count: ")

count = 0

# Loop through string
for i in s:
    if i == ch:    # check match
        count += 1

# Print result
print(count)

# Output:
# Enter string: banana
# Enter character: a
# 3