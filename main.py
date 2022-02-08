""" 
Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
For Example:
const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'i'];
should return false.
-----------
const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'x'];
should return true.

2 parameters - arrays - no size limit
return true or false 
"""

# Now, the very first solution that comes to mind is
# the naive, or brute force solution.
# So let's code that down.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

def brute_force_matching_element(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

print(brute_force_matching_element(array1, array2))