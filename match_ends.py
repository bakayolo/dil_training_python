#!/usr/bin/python

def match_ends(words):
  if not words:
    return 0
  counter = 0
  for word in words:
    w_len = len(word)
    if word and w_len >= 2 and word[0] == word[w_len-1]:
      counter += 1
  return counter
