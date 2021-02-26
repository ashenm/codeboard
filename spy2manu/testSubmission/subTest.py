#!/usr/bin/env python3
#
# SPY2MANU
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

  def test_common(self):
    self.assertEqual(int(self.results.get(0, 0)), 7,
        msg='evaluates 2(250 mod 3) + 5')

  def test_extended(self):
    self.assertEqual(float(self.results.get(1, 0)), 82.896,
        msg='evaluates (3.14(2^5 + 1))/1.25')

  def test_fraction(self):
    self.assertEqual(float(self.results.get(2, 0)), 7,
        msg='evaluates floor(15/2)')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
