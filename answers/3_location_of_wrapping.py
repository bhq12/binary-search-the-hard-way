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

#
#Explanation:
#
#- in essence we want to use binary search to find the smallest element in the array
#
#- if center_value > array[right_pointer]:
#       This means that the smallest value in the array is on the RIGHT HAND SIDE
#       of the center index
#- else if center_value <= array[right_pointer]:
#       In this case our RIGHT HAND SIDE does not contain the smallest value in the array
#       This is because (apart form the shift edge) our values are strictly increasing


def binary_search(array: list[int]):
    left_pointer = 0
    right_pointer = len(array) -1
    while left_pointer < right_pointer:
        center = (left_pointer + right_pointer) // 2
        center_value = array[center]
        if center_value > array[right_pointer]:
            left_pointer = center + 1
        else:
            right_pointer = center

    return left_pointer
