#!/usr/bin/env python3
#
# SPY3MANU
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
      self.results = list(map(float, stream.getvalue().splitlines()))

    super().__init__(*args, **kargs)

  def test_locals(self):
    self.assertTrue(src.main.main.__code__.co_nlocals,
        msg='embodies at least one local variable')

  def test_existing(self):
    self.assertEqual(self.results, [ 1.5 * 2, 2 * 3.14 * 1.5, 3.14 * 1.5 * 1.5 ],
        msg='unaffects existing output')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
