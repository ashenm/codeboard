#!/usr/bin/env python3
#
# SPY5MANU
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

  def test_extchar(self):
    self.assertEqual(self.results.get(0, ''), 'the')

  def test_extphrase(self):
    self.assertEqual(self.results.get(1, ''), 'fox')

  def test_containment(self):
    self.assertEqual(self.results.get(2, ''), 'True')

  def test_transtitle(self):
    self.assertEqual(self.results.get(3, ''), 'The Quick Brown Fox Jumps Over The Lazy Dog')
    self.assertTrue('title' in src.main.main.__code__.co_names)

  def test_concat(self):
    self.assertEqual(self.results.get(4, ''), 'the quick brown fox jumps over the lazy dog while he is asleep')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
