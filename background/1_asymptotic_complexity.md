# Asymptotic Complexity

In order to understand why binary search is an optimal solution to many probelms, we must first tackle how we define "optimal".

In many algorithmic problems, we measure this in one of two ways:
- Average performance
- Asymptotic complexity

## Average Performance
Average performance is a fantastic metric for measuring the real-world performance of an algorithm. However it has a number of disadvantages in a runtime comparison scenario that make it less optimal for formal complexity comparisons


## Asymptotic Complexity
Asymptotic complexity is a mathematical concept related to the theory of limits and infinity.

The general theory behind asymptotic complexity is "how does the performance of the algorithm degrade as our input size trends towards infinity?".

i.e. If our input continues to increase in size, will we continue to see satisfactory performance from this algorithm?

This is known as the "asymptotic complexity", as we want to measure the upper bound (or asymptote) of our algorithm performance under large input sizes (NOTE: in our usage here "upper bound" has a negative connotaion, where a "high" algorithm runtime is considered bad but represents the "upper" scenario)

### Big-O Notation

We typically use a format known as "Big O" notation as the primary measure of asymptotic complexity.

Big O notation is a representation of the UPPER BOUND of performance under a given input.

TODO: More detailed description of "What Big-O is"

```
NOTE: In many scenarios, input size is not expected to grow past a fixed bound, in which case it may be worth considering an algorithm with poorer asymptotic complexity but better expected average runtime. For expample, we may have an algorithm that is guaranteed to complete without 1000 seconds under ANY input size, but a second algorithm that will take approximately 3 seconds per input item.

In this scenario, algorithm one has an O(1) asymptotic complexity, and algorithm two has an O(n) complexity. However, if we were to know that the input will never exceed 100 items, it makes much more sense to use algorithm two as it will take at most 300 seconds to complete the same operation that will always take algorithm one 1000 seconds.
```

Because of the difficulty and time-consuming nature of performing average performance experiments, asymptotic complexity is typically the first (and most-used) measure of algorithm performance.

However there are many many real-world examples of services leveraging a sub-optimal asymptotic complexity algorithm that displays greater real-world performance under expected inputs.

It's important to know the difference between these concepts when making algorithmic decisions, and knowing when to consider sub-optimal asymptotic complexity algorithms where they will be appropriate.
