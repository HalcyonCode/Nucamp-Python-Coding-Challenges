""" 

CHange the print statement to print out the variable stars instead of j.
Change the value so that we add to the stars variable from "1" to "*".
In the first for loop, change the range function's start value from 1 to 0 and the step value from 2 to 1.
In the second, nested for loop, change the range's stop value from 2 to i.
Decrease the indentation for the print statement inside the second for loop, so that it is a part of the first for loop.
 """

stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)