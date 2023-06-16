# This program shows the int number is even or odd and, it's 0, grater than 0 or lower than 0.

# This statement gets number from user.
num = int(input("Please enter an integer number:"))

# This function calculates and shows the answer.
def answer(num):
    # This statements are about when number is 0.
    if num == 0:
        print ("0, even")   

    # This statements are about when number is more than 0.
    elif (num >= 1):
        print ("Grater than 0.")
        if (num % 2 == 0):
            print ("Even")
        else:
            print ("Odd")
        
    # This statements are about when number is lower than 0.
    else:
        print ("lower than 0.")
        if (num % 2 == 0):
            print ("Even")
        else:
            print ("Odd")

# Function call.
answer(num)

# GoodBye message.            
print ("Have a nice time...")

