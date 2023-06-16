"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : # This program converts C(celcius) to F(fahrenheit).
    """
# This program converts C(celcius) to F(fahrenheit).
def convert_c_to_f():

    # This statement gets temperature in celcius from user.
    c = float(input("Please enter a temperature in celcius:"))

    # This statement converts celcius to farenheit.
    f = 9/5*c+32

    # This statement shows the answer.
    print ("Fahrenheit temperature is =>", (f))

# Function call.
convert_c_to_f()