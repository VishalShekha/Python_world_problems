'''
A city has a dam of capacity ‘x’ liters, water comes to the dam from ‘n’ places. Given the value of ‘n’ 
and the quantity of water (in liters and milliliters) that comes from ‘n’ places, Write an algorithm, 
Problem analysis chart, and the corresponding Python code to determine the total amount of water in 
the dam. If dam reaches the full capacity print “DAM_IS_FULL_ALERT”. If the capacity of the dam 
exceeds the maximum limit, then print “DAM_IN_DANGER” else print “DAM_IN_SAFE”. For 
example, if there are three places from which water comes to the dam and the water from place 1 is 2 
liters 500 ml, water from second place is 3 liters 400 ml and water from third place is 1 liter 700 ml 
then the total quantity of water in dam will be 7 liters 600 ml.
'''

x=int(input())
n=int(input())
ltr=0 #Liter
mltr=0 #Milliliter
for i in range(n):
 ltr=ltr+int(input())
 mltr=mltr+int(input())
while mltr>=1000:
 mltr=mltr-1000
 ltr=ltr+1
 
print(ltr)
print(mltr)
if x == ltr and mltr > 0:
 print("DAM_IN_DANGER")
elif x == ltr and mltr == 0:
 print("DAM_IS_FULL_ALERT")
else:
 print("DAM_IN_SAFE")
