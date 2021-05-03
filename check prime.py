
import math
num = int(input("Enter any number: "))
    
if num > 1:    

    for x in range (2,int(math.sqrt(num))+1):
        if num % x == 0:
            print (num, "is not a prime")
            print (num, 'equals', x, "*", num//x)
            break 
    else:
        print (num, "is a prime!")
else:
    print (num, "is not a prime")
