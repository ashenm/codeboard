#!/usr/bin/env python3
#
# SPY7MANU
# https://codeboard.io/projects/190729
# subTest.py
#
# Ashen Gunaratne
# mail@ashenm.ml
#

from io import StringIO
from unittest.mock import patch
from unittest import TestCase, main

import src.main

class subTest(TestCase):

  def __init__(self, *args, **kargs):

    with patch('sys.stdout', new=StringIO()) as stream:
      src.main.main()
      self.results = dict(enumerate(stream.getvalue().splitlines()))

    super().__init__(*args, **kargs)

  def test_sortAsd(self):
    self.assertEqual(self.results.get(0, ''), '''['Anna', 'Christine', 'Danielle', 'Kate', 'Sandy']''',
        msg='sorts list in accenting order')

  def test_sortDsc(self):
    self.assertEqual(self.results.get(1, ''), '''['Sandy', 'Kate', 'Danielle', 'Christine', 'Anna']''',
        msg='sorts lists in descending order')

  def test_insert(self):
    self.assertEqual(self.results.get(2, ''), '''['Sandy', 'Kate', 'Hanna', 'Danielle', 'Christine', 'Anna']''',
        msg='inserts \'Hanna\' into second index')

  def test_remove(self):
    self.assertEqual(self.results.get(3, ''), '''['Kate', 'Hanna', 'Danielle', 'Christine', 'Anna']''',
        msg='removes the first occurrence of \'Sandy\'')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
