# Linear_Search
In Linear search we access the list element once in every iteration, for a list of size N we access the elements up to N times.
If the query element present in the last position (Nth position), than time taken to execute is 'N' time.
If the query element present in first position than we will get the result inn first iteration itself.

Algorithm Analysis:

Complexity and Big O notation: Complexity of an algorithm is the measure of amount of time/ space required by an algorithm for a given input.

In the case of Linear Search:

Complexity is cN (c -> constant depends on the number of operations that we perform in each iteration and time taken to execute the statment).

Space complexity is some constant c' (independent of N), since we just need a single variable position to iterate through the array, 
and it occupies a constant space in the computer's memory (RAM)
