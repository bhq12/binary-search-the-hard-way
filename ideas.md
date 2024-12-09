- binary search where the left and right pointers overflow

- find the MAX true index in this array:
[T,T,T,T,T,F,F,F,F,F]

^ This one is different as you have to set the left_pointer = center rather than (center + 1)
 (right_pointer still gets set to center - 1)
