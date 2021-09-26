""" In a Python code file, write a function named linear_search_dictionary.
Its parameter list should contain a dictionary and a target value.
It should search each value in a given dictionary to see if it matches the target value.
If so, then it will print a success message and return the key of the matched target value.
If the entire dictionary has been searched and no match has been found, it should print a failure message and return the value of None.
"""

def linear_search_dictionary(the_dictionary, target):
    for x, y in the_dictionary.items():
        if y == target:
            print("Found at key", x)
            return x
    print("Target is not in the dictionary")
    return None

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)