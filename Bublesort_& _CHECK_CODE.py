# BUBLE SORT

import math
import random

numlist = []

for i in range(5):
    numlist.append(random.randrange(1,10))

i = len(numlist)-1

while i > 1:
    j= 0
    while j < i:
        print (" In numlist Is {} > {}". format(numlist[j], numlist[j+1]))
        #swap the smaller value first and greater value next
        if numlist [j] > numlist[j+1]:
            #to check if we are switching 
            print ('switch ')

            
            temp = numlist[j]
            numlist [j] = numlist[j+1]
            numlist[j+1]= temp
        else:
            print('Dont switch ')

        j += 1
        for k in numlist:
            print (k , end=", ")
        print()
        
    #to know one cycle
    print('END OF ROUND')    
    i -= 1

for k in numlist:
    print (k , end=", ")
print()

