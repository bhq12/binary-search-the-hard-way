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

def binary_search(array: list[int], target_value: int):
    left_pointer = 0
    right_pointer = len(array) - 1
    best_candidate = -1

    while left_pointer <= right_pointer:
        center = (left_pointer + right_pointer) // 2
        center_value = array[center]
        if center_value < target_value:
            best_candidate = center
            left_pointer = center + 1
        else:
            right_pointer = center - 1
    return best_candidate

