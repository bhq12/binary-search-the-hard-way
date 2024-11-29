############################################################
############################################################
'''
The original, but recursive!

Implement standard binary search using a recursive function

Input:
array - A sorted list of integers
target_value - the integer to find in the array

Note: if the target_value is not in the array, please return -1

'''
############################################################
############################################################

def binary_search(array: list[int], target_value: int):
    def recursive_binary_search(array, left_pointer, right_pointer, target_value):
        if right_pointer < left_pointer:
            return -1
        middle = (left_pointer + right_pointer) // 2
        middle_value = array[middle]

        if middle_value == target_value:
            return middle
        elif middle_value < target_value:
            left_pointer = middle + 1
        else:
            right_pointer = middle - 1
        return recursive_binary_search(array, left_pointer, right_pointer, target_value)

    return recursive_binary_search(array, 0, len(array) - 1, target_value)

