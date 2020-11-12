#!/usr/bin/env python3
#
# SPY1MANU
# https://codeboard.io/projects/189264
# subTest.py
#
# Ashen Gunaratne
# mail@ashenm.ml
#

from io import StringIO
from re import match
from unittest.mock import patch
from unittest import TestCase, main

import src.main

class subTest(TestCase):

  def __init__(self, *args, **kargs):

    with patch('sys.stdout', new=StringIO()) as stream:
      src.main.main()
      self.results = dict(enumerate(stream.getvalue().splitlines()))

    super().__init__(*args, **kargs)

  def test_hello(self):
    self.assertEqual(self.results.get(0, ''), 'hello, world!', msg='prints "hello, world!"')

  def test_name(self):
    self.assertIsNotNone(match(r'^this is .*\'s Python script!$', self.results.get(1, '')),
      msg='prints "this is <your name>\'s Python script!"')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
