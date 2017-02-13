#!/usr/bin/python

def verbing(s):
  if not s or len(s) < 3:
    return s
  elif s[-3:] == 'ing':
    return s + 'ly'
  else:
    return s + 'ing'
