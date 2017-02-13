#!/usr/bin/python

def mix_up(a, b):
  if not a:
    return b
  elif not b:
    return a
  else:
     a_list = list(a)
     b_list = list(b)
     a_list[0] = b_list[0]
     a_list[1] = b_list[1]
     a_list_2 = list(a)
     b_list[0] = a_list_2[0]
     b_list[1] = a_list_2[1]
  return ''.join(a_list) + ' ' + ''.join(b_list)
