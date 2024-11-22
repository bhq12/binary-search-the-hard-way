############################################################
############################################################
'''
The original, the classic.
Embrace the first-year computer science nostalgia as you
implement binary search the right way

Input:
array - A sorted list of integers
target_value - the integer to find in the array

Note: if the target_value is not in the array, please return -1

'''
############################################################
############################################################


def binary_search(array: list[int], target_value: int):
    left_pointer = 0
    right_pointer = len(array) - 1

    #NOTE: <= is used when we are converging on the correct value
    while left_pointer <= right_pointer:
        center = (left_pointer + right_pointer) // 2
        center_val = array[center]
        if center_val < target_value:
            left_pointer = center + 1
        elif center_val == target_value:
            return center
        else:
            right_pointer = center - 1
    #NOTE: The use of <= means if we reach this point, the target_value
    # is not in the array
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 2

    array = [0, 1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 3
    
    array = [-1, 1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 3
    
    array = range(10**15) 
    assert binary_search(array, 3000000) == 3000000
    assert binary_search(array, 10**12) == 10**12

    array = []
    assert binary_search(array, 1) == -1
