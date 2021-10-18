# Problems Encountered in the Wild

## Problem 1 - Uber

You are given an array of integers `numbers`. Your task is to count the number of distinct pairs `(i,j)` such that `0 <= i < j < numbers.length`, `numbers[i]`, and `numbers[j]` have the same number of digits, and only one of the digits differ between `numbers[i]` and `numbers[j]`

Example:

For `numbers = [1, 151, 241, 1, 9, 22, 351]`, the output should be `almostEqualNumbers(numbers) = 3`

- `numbers[0] = 1` differs from `numbers[4] = 9` on the one and only digit in both numbers
- `numbers[1] = 151` differs from `numbers[6] = 351` on the first digit
- `numbers[3] = 1` differs from `numbers[4] = 9` on the one and only digit in both numbers

**Note** that `numbers[0] = 1` and `numbers[3] = 1` do not differ from each other at all and thus do not count as a valid pair

[Solution](./Uber_Distinct_Pairs.py)

<hr>
