from helpers.assert_with_message import assert_with_message
from helpers.custom_boolean_iterators import (
    CustomBooleanTrueIterator,
    CustomBooleanFalseIterator,
    CustomBooleanTrueFalseIterator
)
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
    # implement your binary search here!
    raise NotImplementedError


if __name__ ==  '__main__':
    array = [True, True, True, False, False, False]
    assert_with_message(binary_search(array), 2)

    array = [True, True, True, True, False, False, False]
    assert_with_message(binary_search(array), 3)

    array = [True, True, True, True, False]
    assert_with_message(binary_search(array), 3)

    array = [True, False, False, False]
    assert_with_message(binary_search(array), 0)

    array = [False, False, False]
    assert_with_message(binary_search(array), -1)

    array = CustomBooleanTrueFalseIterator()
    assert_with_message(binary_search(array), 9)

    array = CustomBooleanTrueIterator()
    assert_with_message(binary_search(array), len(array) - 1)

    array = CustomBooleanFalseIterator()
    assert_with_message(binary_search(array), -1)

    array = []
    assert_with_message(binary_search(array), -1)
 
    print("Congratulations! Your binary search implementation was correct 🎉")

