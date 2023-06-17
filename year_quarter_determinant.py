"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : This program shows in which quarter of the year the selected month of the user is
    """
# This program shows in which quarter of the year the selected month of the user is

# This statement gets the number of month from user
month = int(input("""1 = January
2 = february
3 = March
4 = April
5 = May
6 = Jun
7 = July
8 = August
9 = September
10 = October
11 = November
12 = December
Please enter a number from 1 to 12 for choosing month:"""))
    
# This function checks the input is True or False
def range_detection1():
    while month >= 13:
        print("Month number is wrong.")
        int(input("Please enter a number from 1 to 12 for choosing month:"))

# This function checks the input is True or False
def range_detection2():
    while month <= 0:
        print("Month number is wrong.")
        int(input("Please enter a number from 1 to 12 for choosing month:"))
    
# this statement is function call
range_detection1()
range_detection2()

# This function chooses which quarter is choosed number is
def which_quarter():
        
    # This statements show the answer when the month choosed is about 1st quarter of the year
    if (month>=1) and (month<=3):
        print("You choosed a month in 1st quarter of the year")
        
    # This statements show the answer when the month choosed is about 2nd quarter of the year
    elif (month>=4) and (month<=6):
        print("You choosed a month in 2nd quarter of the year")
        
    # This statements show the answer when the month choosed is about 2nd quarter of the year
    elif (month>=7) and (month<=9):
        print("You choosed a month in 3rd quarter of the year")

    # This statements show the answer when the month choosed is about 2nd quarter of the year
    else:
        print("You choosed a month in 4th quarter of the year")

# This statement is function call
which_quarter()

# This statement shows goodbye message
print("Have a nice time, GoodBye!")