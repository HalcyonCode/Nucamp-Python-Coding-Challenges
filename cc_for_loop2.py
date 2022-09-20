""" 
Fix the for loop in range(), starting at 0 and ending at 6, incrementing by 1.
If x is equal to 0 or 6 print out one asterisk; if  x is equal to 1 or 5 print out two asterisks;
if x is equal to 2 or 3 print out 3 asterisks. Otherwise prinr out 4 asterisks.
 """

for x in range(0, 6, 1):
    if x == 0 or x == 6:
        print("*")
    elif x == 1 or x == 5:   
        print("**")
    elif x == 2 or x == 3:
        print("***")
    else:    
        print("****")