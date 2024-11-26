from helpers.assert_with_message import assert_with_message
############################################################
############################################################
'''
Given a sorted array that has been shifted by an arbitrary number of digits
Find the location of the start of the array

For example the array:
[1, 2, 3, 4, 5]
shifted by two digits to the left gives
[3, 4, 5, 1, 2]
the location of the start of the array is now at index 3

Input:
array - A (potentially shifted) sorted list of integers

Note: if the array has not been shifted, please return 0

Second note: Negative indexes are correct i.e. for the
example above the correct answer is index 3 and not
index -2

'''

def binary_search(array: list[int]):
    # implement your binary search here!
    raise NotImplementedError


if __name__ ==  '__main__':
    array = [1, 2, 3, 4, 5]
    assert_with_message(binary_search(array), 0)

    array = [3, 4, 5, 0, 1, 2]
    assert_with_message(binary_search(array), 3)

    array = [2, 3, 4, 5, 6, -1]
    assert_with_message(binary_search(array), 5)

    array = [-1, 1, 2, 3, 4, 5]
    assert_with_message(binary_search(array), 0)

    array = range(10**15) 
    assert_with_message(binary_search(array), 0)

    array = []
    assert_with_message(binary_search(array, 1), 0)

    print("Congratulations! Your binary search implementation was correct 🎉")

