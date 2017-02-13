#!/usr/bin/python

def fix_start(s):
  if not s:
    return ''
  else:
    first_s = s[0]
    result = list(s.replace(first_s, '*'))
    result[0] = first_s
    return ''.join(result)
