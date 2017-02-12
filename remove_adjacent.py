#!/usr/bin/python

def remove_adjacent(nums):
  if not nums:
    return []
  deduplicate_nums = []
  for num in nums:
    if not is_in(num, deduplicate_nums):
      deduplicate_nums.append(num)
  return deduplicate_nums

def is_in(num, nums):
  if not nums:
    return False
  for n in nums:
    if (n == num):
      return True

