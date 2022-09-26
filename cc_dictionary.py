""" below the dictionary declaration, write a function named print_total_snowfall with a parameter of inches_snow.
Inside this function, declare a variable named total_inches and initialize its value to 0.
Then, write a for loop inside the function that iterates over the values of inches_snow, with an iteration variable of inches.
Inside this for loop, increment the variable total_inches by the value of inches.
Once the for loop ends, and still inside the function, print "Total snowfall inches: ", followed by the value of total_inches.
Outside of and below the print_total_snowfall() function, call the function, passing in the inches_snow dictionary as the argument. 
At this point, if you ran your code, it should output this:


Next, use what you know of the input() function to prompt the user to answer the question, "How many inches of snow fell on Thursday?"
Save this value to the dictionary with the key of "Thursday". 
Below where you used the input() function, call the print_total_snowfall() function once again with the same argument.
Save and run the code. The output should look similar to this:
"""


inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)

print_total_snowfall(inches_snow)
new_value = input("How many inches of snow fell on Thursday?: ")
inches_snow["Thursday"] = int(new_value)

print_total_snowfall(inches_snow)