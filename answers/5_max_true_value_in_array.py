############################################################
############################################################
'''
Given an array of boolean values containing a set of True values followed by a set of False values,
find the index of the maximum True value in the array

- For example, the following array has a final True value index of 4
[T,T,T,T,T,F,F,F,F,F]

Input:
array - An array of booleans containing True values, followed by False values

Output:
index - The index of the final True value in the array

Note: If the array does not contain any True values, return -1

'''

def binary_search(array: list[bool]) -> int:
    left_pointer = 0
    right_pointer = len(array) - 1
    highest_index = -1

    while left_pointer <= right_pointer:
        center = (left_pointer + right_pointer + 1) // 2
        center_value = array[center]

        if center_value:
            left_pointer = center + 1
            if center > highest_index:
                highest_index = center
        else:
            right_pointer = center - 1
    return highest_index
