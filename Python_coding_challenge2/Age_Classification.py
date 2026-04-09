age = int(input("Enter age: "))

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Output:
# Enter age: 65
# Senior