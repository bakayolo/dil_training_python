#!/usr/bin/python

def front_x(words):
  if not words:
    return []
  x_words = []
  sorted_words = []
  for word in words:
    if word and word[0] == 'x':
      x_words = sort(word, x_words)
    else:
      sorted_words = sort(word, sorted_words)
  return x_words + sorted_words

def sort(new_word, words):
  sorted_words = list(words)
  if not sorted_words:
    sorted_words.append(new_word)
    return sorted_words
  index = 0;
  w_len = len(words)
  while index < w_len:
    if (new_word < words[index]):
      break
    index += 1
  sorted_words.insert(index, new_word)
  return sorted_words
