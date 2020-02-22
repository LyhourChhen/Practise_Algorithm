#!usr/bin/python3
# Reverse String

'''
Create the function which can enter the string and reverse it back ! 
'''

print("Reverse String")

# My Approuch which totally messy bullshit and it doesn't not work : ((((

def reverseString(arg):
    print("Normal String : ", arg)
    #Find how to many in range first
    rangeAmount = 0
    result = "lala"
    for i in arg:
        rangeAmount = i + i
        return rangeAmount
    #reverse loop
    for i in range(rangeAmount,1,-1):
        return
    return result
print("result :", reverseString("LyhourChhen"))

#method 1 (slicing)

# Slicing in python can be easily to reverse the index ! :S

str="Python" # initial string
stringlength=len(str) # calculate length of the list => 6
#stringname[stringlength::-1] (1st) 
slicedString=str[stringlength::-1] # slicing (2nd)
print (slicedString) # print the reversed string

#method 2 (loop)

str = "Python" # initial string
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0: 
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string


#method 3 (join)
str = 'Python' #initial string
reversed=''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string

###
