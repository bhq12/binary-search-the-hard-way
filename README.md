# Learn Binary Search the Hard Way!

Sure, binary search seems easy...

Just use a sorted array, make a left and right pointer, and split the array in half each iteration until you find the target. Easy right?

Wrong!

I made this tool because I always forget how to adjust my binary search edge cases for different scenarios:

- How do you use binary search to get the highest number less than target?
- How do you use binary search to find the first instance of target in the array?
- How do you use binary search to find the smallest value greater than the target when the target is not present in the array?

I always mess these up, use this tool to help you not mess them up too!

If you are a newcomer to binary search, don't worry, we have background and easy problems too to help bring you up to speed!

## Background
If you're currently unfamiliar with binary search as a concept, or it's been a long time since you've revisited the concept, feel free to read through the concepts in ./background first (and please raise a pull request and contribute back if there is anything missed or additional detail that would be helpful!

## Setup and dependencies
This project is intentionally created with no package dependencies for simple running on any system. All that is required is that you have a recent-ish python 3.x version installed. It is recommended that this version is python 3.10+, but I suspect it will work on older versions as well (I just haven't tested with the typehints etc.)

## How to use

There are two primary directories in this repo, kept separate to reduce the likelihood of accidentally glimpsing answers while attempting the questions.

### ./problems
You should go here first! This is where the problems are kept, Read the problem description at the top and then attempt the solution by completing the binary_search() function definition

```
def binary_search...
```

All problem definitions have prefilled test cases containing common scenarios and edge cases. You're welcome to either look at or ignore the scenarios while thinking about the problem, they're at the bottom of the file in the ```if __name__ == '__main__'``` block.

#### Running the scenarios

Running the scenarios is as simple as executing the python files like so:

```
python problems/1_normal_binary_search.py
```
Alternatively it can also be run from inside the problems directory, it doesn't really matter.

```
cd problems
python 1_normal_binary_search.py
```
If your implementation is correct and passes all the scenarios you should see the message

```
Congratulations! Your binary search implementation was correct
```

If your implementation is incorrect, exception details will be logged to the console and you should be able to debug from there.


### Solutions

Solutions are provided, but it is highly recommended that you at least attempt the problems yourself before looking at the solutions.

Obviously if you're completely stuck, feel free to look at the solution for learning purposes.

I recommend if you find yourself needing to look at the solution, read it once and understand how the problem is being solved. Then come back after a short period of time (say 10 minutes) and re-implement the solution by yourself.

The solutions are intentionally kept separate from the problems in order to encourage you to do this :)


