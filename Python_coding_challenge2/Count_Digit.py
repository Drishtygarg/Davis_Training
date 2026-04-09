#This program counts number of digits in a number

#Take input
num = int(input("Enter number: "))

count = 0 #counter variable

#Loop untill number becomes 0
while num > 0:
    count += 1  #increase count
    num = num // 10 #remove last digit

    #print result
    print(count)

    #Output:
    #Enter number: 45678
    #5