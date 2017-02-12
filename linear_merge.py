#!/usr/bin/python

def linear_merge(list1, list2):
  if not list1:
    return list2
  if not list2:
    return list1
  l1_len = len(list1)
  l2_len = len(list2)
  merged_list = []
  i1 = 0
  i2 = 0
  while i1 < l1_len:
    if i2 >= l2_len or list1[i1] < list2[i2]:
      merged_list.append(list1[i1])
      i1 += 1
    else:
      merged_list.append(list2[i2])
      i2 += 1
  while i2 < l2_len:
    merged_list.append(list2[i2])
    i2 += 1
  return merged_list