"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : This program shows (the amount of money Joe paid for the stock),
                    (the amount of commission Joe paid his broker when he bought the stock),
                    (the amount for which Joe sold the stock),
                    (the amount of commission Joe paid his broker when he sold the stock),
                    (the amount of money that Joe had left when he sold the stock and paid his broker.
                    If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.)
                    """

# This statement is about the number of shares that Joe purchase.
stock = 2000

# This statement is about how much Joe paid for each stock.
per_stock = 40

# This statement is about perch.
purch = stock*per_stock

# This statement is about 1st commission.
comm1 = purch*0.03

# This statement is about sold.
sold = stock*per_stock

# This statement is about 2nd commission.
comm2 = sold*0.03

# This function is about geting stock.
def get_stock():
    purch = stock*per_stock
    print ("The amount of money Joe paid for the stock is", (purch),("$"))

# This function is about commission Joe paid his broker 1st time.
def commission_1(purch):
    comm1 = purch*0.03
    print ("The amount of commissin Joe paid his broker when he bought the stock is", (comm1),("$"))

# This function is about solding stock.
def sold_stock(stock):
    per_stock = 42
    sold = stock*per_stock
    print ("The amount of money Joe sold stocks is", (sold),("$"))

# This function is about commission Joe paid his broker 2nd time.
def commission_2(sold):
    comm2 = sold*0.03
    print ("The amount of commission Joe paid his broker when he sold the stock is", (comm2),("$"))      

        # This function is about how much Joe benefited or had harm
def benefit_or_harm(sold, comm1, comm2, purch):
    remain = sold-(comm1 + comm2)
    print ("Joe has",(remain),"$")
    if remain > purch:
        print ("Joe's net money is",((sold)-(purch)),("$"))
        print ("Hooray! Joe has benefited!")
    else:
        print ("Joe's lost money is",((purch)-(remain)),("$"))
        print ("Sadly, Joe has done harm.")
        print ("Have a nice time, goodbye")

# Function call.

get_stock()

commission_1(purch)

sold_stock(stock)

commission_2(sold)

benefit_or_harm(sold, comm1, comm2, purch)