############################################################
############################################################
'''
A common modification!

Please return the largest value in the array that is smaller than the target.

Input:
array - A sorted list of integers
target_value - the integer to find in the array

Note: - If there are no values in the array smaller than the target, please return -1

'''
############################################################
############################################################

# step 1: find the target in the array
# step 2: get the value at index target_index - 1
def binary_search(array: list[int], target_value: int):
    left_pointer = 0
    right_pointer = len(array) - 1
    target_index = -1

    while left_pointer <= right_pointer:
        center = (left_pointer + right_pointer) // 2
        center_value = array[center]
        if center_value == target_value:
            target_index = center
            break
        elif center_value < target_value:
            left_pointer = center + 1
        else:
            right_pointer = center - 1

    if target_index == -1 or target_index == 0:
        return target_index

    return array[target_index - 1]

