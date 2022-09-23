""" 
Reverse the string that is passed into the str paramenter.
 """

def reverse(str):
    return str[::-1]

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))