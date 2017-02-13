#!/usr/bin/python

def not_bad(s):
  if not s:
    return ''
  if 'not' in s and 'bad' in s:
    not_index = s.index('not')
    bad_index = s.index('bad')
    if not_index < bad_index:
      return s[:not_index] + 'good' + s[bad_index+3:len(s)]
    else:
      return s
  else:
    return s