#!/usr/bin/python

def both_ends(s):
  if not s or len(s) < 2:
    return ''
  else:
    s_len = len(s)
    return s[0] + s[1] + s[s_len-2] + s[s_len-1]
