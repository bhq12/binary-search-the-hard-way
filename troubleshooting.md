In most scenarios, you should be able to debug what is happening should you encounter an issue during execution. However, some problems are more obscure to debug, here is a list of some of these more obscure problems in case you are stuck:

# Obscure Problems

## Code not exiting
If you find that after executing the problem

```
python problems/1_normal_binary_search.py
```

That your system hangs and no output is logged to console, it is likely that you have accidentally created an infinite loop.

Check your __while__ loop condition and iteration logic to ensure that your implementation allows for the loop to exit.

## Overflow on 32-bit devices
There are two most-likely causes for seeing an overflow error during execution.

The first (most likely) is you're working on a regular 64-bit modern system and you're calculating the center value inside the while loop without considering overflows. The fix for this is to convert your line similar to:

```
center_index = (left_pointer + right_pointer) // 2
```
To perform this same calculation in a more overflow-safe manner:

```
center_index = left_pointer + (right_pointer - left_pointer) // 2
```
By performing a subtraction rather than addition during intermediate steps we prevent the risk of overflow while adding left_pointer and right_pointer.


Another possible issue is that you're runnning this solution on a 32-bit system, in which case the large-number test scenarios will result in an overflow before the while loop is even reached.

This will result in an error such as:
```
right_pointer = len(array) - 1
OverflowError: Python int too large to convert to C ssize_t
```
In this case you will have to update the scenarios manually, in particular look for the 10\*\*15 lines in the tests (at some point in the future I may find the time to update the scenarios to detect the word-size of the system being run on and act accoringly, but this is the workaround for now)
