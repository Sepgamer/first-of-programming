"""
    *   Developer   : Sepehr Hosseini
    *   Email       : Sepgamer87@Gmail.Com
    *   Description : This program shows how much calories do you burn after 10, 15, 20, 25 and 30 mins running on special tredmill
    """
# This program shows how much calories do you burn after 10, 15, 20, 25 and 30 mins running on special tredmill

# This statement is about how much calories you burn after 1 minutes on tredmill
base_cal = 4.2

# This function calculates how much calories you burn after 10, 15, 20, 25 and 30 mins running on tredmill

# This statement shows Respectively after 10, 15, 20, 25 and 30 minutes running on tredmill
def time_run():
    print("Respectively after 10, 15, 20, 25 and 30 minutes running on tredmill")

def calories_burn():
    for time in [10, 15, 20, 25, 30]:

        # This statement calculates calories burned after 10, 15, 20, 25 and 30 mins running on tredmill
        burns = base_cal * time

        # This statement shows calories burned after 10, 15, 20, 25 and 30 mins running on tredmill
        print("You burn", burns,"calories")
        print("-----------------------")

# This statements are function call
time_run()
calories_burn()