#!/usr/bin/env python3
#
# <EXERCISE_REFERENCE>
# <CODEBOARD_PROJECT_URI>
# subTest.py
#
# Ashen Gunaratne
# mail@ashenm.ml
#

from io import StringIO
from unittest.mock import patch
from unittest import TestCase, main
import xml.etree.ElementTree as ElementTree

import src.main

class subTest(TestCase):

  def __init__(self, *args, **kargs):

    with patch('sys.stdout', new=StringIO()) as stream:
      src.main.main()
      self.results = stream.getvalue()

    try:
      self.root = ElementTree.fromstring(self.results)
    except ElementTree.ParseError as error:
      self.root = error

    super().__init__(*args, **kargs)

  def test_alpha(self):
    self.assertNotIsInstance(self.root, ElementTree.ParseError, msg=str(self.root))

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
