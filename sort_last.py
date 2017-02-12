#!/usr/bin/python

def sort_last(tuples):
  if not tuples:
    return []
  sorted_tuples = []
  for t in tuples:
      sorted_tuples = sort(t, sorted_tuples)
  return sorted_tuples

def sort(new_tuple, tuples):
  sorted_tuples = list(tuples)
  if not sorted_tuples:
    sorted_tuples.append(new_tuple)
    return sorted_tuples
  index = 0;
  t_len = len(tuples)
  t_lastindex = len(new_tuple)-1
  while index < t_len:
    t_index = tuples[index]
    if (new_tuple[t_lastindex] < t_index[len(t_index)-1]):
      break
    index += 1
  sorted_tuples.insert(index, new_tuple)
  return sorted_tuples
