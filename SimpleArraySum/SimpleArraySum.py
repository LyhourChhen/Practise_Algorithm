#!/usr/bin/python3
# SimpleArraySum

'''
Sum up of giving value in array = [1,2,3] sould answer by 6 back !
'''

print("Simple Array Sum")
array = [1,2,3]

def arraySum(array):
    initValue = 0;
    for i in array:
          initValue = i  + i
    return initValue
print("stdout : ",arraySum(array))

