# (inquiry i -- kattis solution)
## Pardon the terrible variable names, this code is repurposed from a programming contest

c = input()                    ## Input number of ints in array
nums=[0]*c                     ## Initialize array of size c

for i in range(c):             ## Loop to add input to nums array
    nums[i] = int(input())

maximum = 0
left = 0
right = 0

for j in nums:
    right += j

for x in nums:                ## Mathematical trickery
    left += pow(x,2)
    right -= x
    temp = left * right
    
    if(temp>=maximum):
        maximum = temp
    
print(maximum)
