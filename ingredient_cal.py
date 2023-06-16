"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : # This program shows ingredient of number of cookies requested.
    """

# This statement gets the number of cookies that user want to make from user.
num_cookies = int(input('Please enter the number of cookies you want to make:'))
     
# This function checks input number.
def check_num_cookies():
    global num_cookies
    while num_cookies < 0:
        print("Error. Your input number must be 0 or more")
        int(input('Please enter the number of cookies you want to make:'))

    # Function call.
    check_num_cookies()

    # This if statements shows the ingredients need.
def answer():
        if num_cookies == 48:
            print ("The number of cups of sugar you need is 1.5")
            print ("The number of cups of butter you need is 1")
            print ("cups of float you need is 2.75")
        else:
            s = 1.5*num_cookies/48
            b = 1*num_cookies/48
            f = 2.75*num_cookies/48
            print (f'cups of sugar you need is {s:,.1f} cups')
            print (f'cups of butter you need is {b:,.1f} cups')
            print (f'cups of float you need is {f:,.1f} cups')

# Function call.
answer()