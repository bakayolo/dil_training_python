#!/usr/bin/python

from match_ends import match_ends
from front_x import front_x
from sort_last import sort_last
from remove_adjacent import remove_adjacent
from linear_merge import linear_merge

def test(got, expected):
  prefix = 'OK' if got == expected else ' X'
  # !r prints a Python representation of the strings (complete with quotes)
  print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
      ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
      ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
      ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
      [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
      [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
      [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

  print
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
      ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
      ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
      ['aa', 'aa', 'aa', 'bb', 'bb'])

main()