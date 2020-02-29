#!usr/bin/python3

import time
from math import pi

name = "My name is LyhourChhen"
for i in name:
    print(i,end="")
    time.sleep(0.1)


#1
print("---> 1")

print("Enter each subject score ")
khmer = int(input("Khmer: "))
english = int(input("english: "))
math = int(input("math: "))
physic = int(input("physic: "))
cpp = int(input("cpp: "))
total = khmer + english + math + physic + cpp
avg = total * 5 /100
print("Result : ",total,"\nAverage:", avg)

print("---> 2")
#Formula A= wl
# P = 2(l+w)
print("Find the Area and Parameter of retrangle")
def area(w, l):
    return w&l
def parameter(w,l):
    return 2*(w+l)
    
w = int(input("Enter width: "))
l = int(input("Enter length: "))
print("Area:",area(w,l))
print("Parameter", parameter(w, l))

print("---> 3")
#formula A=πr2
print("Find area of circle")
def areaCircle(r):
    return (pi*r**2)*2
r = int(input("Enter radius: "))
print("Area of Circle", areaCircle(r))

