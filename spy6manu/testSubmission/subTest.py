#!/usr/bin/env python3
#
# SPY6MANU
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

  def test_sum(self):
    self.assertEqual(float(self.results.get(0, 0)), 107.5)

  def test_average(self):
    self.assertEqual(round(float(self.results.get(1, 0)), 2), 17.92)

  def test_sliceStart(self):
    self.assertEqual(self.results.get(2, ''), '[10, 15.5, 17]')

  def test_sliceEnd(self):
    self.assertEqual(self.results.get(3, ''), '[19, 21, 25]')

  def test_sliceOdd(self):
    self.assertEqual(self.results.get(4, ''), '[15.5, 19, 25]')

  def test_sliceEven(self):
    self.assertEqual(self.results.get(5, ''), '[10, 17, 21]')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
