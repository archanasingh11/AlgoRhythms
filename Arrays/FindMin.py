#Find The Lowest Value in an Array

#Time Complexity = O(n)


arr= [34,67,32,76,58,63,4]


minVal= arr[0]

for i in arr:
    if i<minVal:
        minVal= i

print (minVal)