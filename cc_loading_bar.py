""" 
Update the arguements for the range function such that when the iteration variable amount_loaded is printed 
inside the for loop, it will print the value from 0 to 100 (inclusive), incrementing by 5.
Then add conditional statements to check that amount_loaded is equal to 25, 50, 75, & 100, such that:
If = to 25 print "1/4 of the way there"
If = to 50 print "1/2 of the way there"
If = to 75 print "3/4 of the way there"
If = to 100 print "Loading complete."
 """


for amount_loaded in range(0, 101, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("1/4 of the way there")
    elif amount_loaded == 50:
        print("1/2 of the way there")
    elif amount_loaded == 75:
        print("3/4 of the way there")
    elif amount_loaded == 100:
        print("Loading compelete!")    