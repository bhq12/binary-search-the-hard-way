from helpers.assert_with_message import assert_with_message
############################################################
############################################################
'''
The original, but recursive!

Implement standard binary search using a recursive function

Input:
array - A sorted list of integers
target_value - the integer to find in the array

Output:
index - The index of target_value in the array
Note: if the target_value is not in the array, please return -1

'''
############################################################
############################################################


def binary_search(array: list[int], target_value: int) -> int:
    # implement your binary search here!
    raise NotImplementedError


if __name__ ==  '__main__':
    array = [1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 2)

    array = [0, 1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 3)

    array = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
    assert_with_message(binary_search(array, 1), 5)

    array = [-1, 1, 2, 3, 4, 5]
    assert_with_message(binary_search(array, 3), 3)

    array = range(10**15) 
    assert_with_message(binary_search(array, 3000000), 3000000)
    assert_with_message(binary_search(array, 10**12), 10**12)

    array = []
    assert_with_message(binary_search(array, 1), -1)

    print("Congratulations! Your binary search implementation was correct 🎉")

