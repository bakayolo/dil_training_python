#!/usr/bin/python

def front_back(a, b):
  if not a:
    return b
  elif not b:
    return a
  else:
    a_length = len(a)
    a_half_index = a_length / 2
    if a_length % 2 != 0:
      a_half_index = a_half_index + 1
    b_length = len(b)
    b_half_index = b_length / 2
    if b_length % 2 != 0:
      b_half_index = b_half_index + 1
    return a[:a_half_index] + b[:b_half_index] + a[a_half_index:] + b[b_half_index:]