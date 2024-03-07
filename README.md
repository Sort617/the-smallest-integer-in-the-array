# Find Smallest Integer Function

## Overview
This repository contains a Python function `find_smallest_int` designed to find and return the smallest integer in an array of integers. It is a straightforward implementation that iterates through the given array and keeps track of the smallest integer encountered.

## Function Description

### `find_smallest_int(arr)`
- **Parameters**: `arr` (list): An array of integers.
- **Returns**: The smallest integer found in `arr`.

### How It Works
1. Initializes a variable `s` to the first element of the array `arr`.
2. Iterates through each element of the array.
3. Compares the current smallest value `s` with each element, updating `s` if a smaller element is found.
4. After completing the iteration, returns the smallest value `s`.

## Testing
The function is tested using a series of assertions that pass various arrays to `find_smallest_int` and compare the output to the expected smallest value. Test cases include arrays with positive numbers, negative numbers, and a mix of both.

### Test Cases
1. `test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)`
2. `test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)`
3. `test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)`

Ensure your testing framework supports the `test.assert_equals` method for these tests to function correctly.
