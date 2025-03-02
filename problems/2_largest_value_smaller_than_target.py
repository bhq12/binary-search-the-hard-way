from helpers.assert_with_message import assert_with_message
############################################################
############################################################
'''
A common modification!

Please return the largest value in the array that is smaller than the target.

Input:
array - A sorted list of integers
target_value - the integer to find in the array

Output:
index - the index of the largest value in the array that is smaller than target_value

Note: - If there are no values in the array smaller than the target, please return -1

'''
############################################################
############################################################

def binary_search(array: list[int], target_value: int) -> int:
    return NotImplementedError

if __name__ ==  '__main__':
    array = [1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 2)

    array = [0, 1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 2)

    array = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
    assert_with_message(binary_search(array, 1), 0.1)

    array = [-1, 1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 2)

    array = range(10**15) 
    assert_with_message(binary_search(array, 3000000), 2999999)
    assert_with_message(binary_search(array, 10**12), (10**12 - 1))

    array = []
    assert_with_message(binary_search(array, 1), -1)

    print("Congratulations! Your binary search implementation was correct 🎉")
