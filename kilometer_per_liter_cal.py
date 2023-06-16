"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : # This program shows car's Kilometer-Per-Liter(KPL)
    """
# This program show car's Kilometer-Per-Liter(KPL)
def show_kpl():
    
    # This statement gets kilometer arived from user.
    km = float(input("Please enter the kilometers traveled by the car:"))

    # This statement gets liter used from user.
    lit = float(input("Please enter the number of liters consumed by the car:"))

    # This statements show car's Kilometer-per-Liter
    kpl = km/lit
    print ("Your car's Kilometer-Per-Liter is", (kpl))

# Function call.
show_kpl()
