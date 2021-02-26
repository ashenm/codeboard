#!/usr/bin/env python3
#
# SPY4MANU
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

  def test_int(self):
    self.assertEqual(self.results.get(0, ''), '''<class 'int'>''')

  def test_float(self):
    self.assertEqual(self.results.get(1, ''), '''<class 'float'>''')

  def test_bool(self):
    self.assertEqual(self.results.get(2, ''), '''<class 'bool'>''')

  def test_str(self):
    self.assertEqual(self.results.get(3, ''), '''<class 'str'>''')

  def test_efloat(self):
    self.assertEqual(self.results.get(4, ''), '''<class 'float'>''')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
