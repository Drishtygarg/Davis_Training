'''4. Remove Duplicate Lines
A file contains repeated lines due to logging errors.
Create a new file with only unique lines (preserve order).'''

seen = set()

with open("input.txt", "r") as source:
    with open("output.txt", "w") as dest:
        
        for line in source:
            if line not in seen:
                dest.write(line)
                seen.add(line)

print("Duplicate lines removed successfully!")