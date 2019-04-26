# https://www.codewars.com/kata/compute-the-largest-sum-of-all-contiguous-subsequences/train/python
def largest_sum(arr):
    max_sum = temp_sum = 0
    for i in arr:
        temp_sum += i
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return max_sum
