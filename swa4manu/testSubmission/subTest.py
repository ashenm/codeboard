#!/usr/bin/env python3
#
# SWA4MANU
# https://codeboard.io/projects/220595
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
from utilities import xml

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

  def test_beta(self):
    titles = self.root.findall('head/title')
    self.assertTrue(all([ len(titles) == 1, xml.innerText(titles[0]) == 'SWA4MANU' ]),
        msg='embodies exactly one title with valid content')

  def test_bold(self):
    bolds = self.root.findall('body/p/b')
    self.assertTrue(all([ len(bolds) == 1, xml.innerText(bolds[0]) == 'b element' ]),
        msg='embodies exactly one boldface element with valid content')

  def test_italic(self):
    italics = self.root.findall('body/p/i')
    self.assertTrue(all([ len(italics) == 1, xml.innerText(italics[0]) == 'i element' ]),
        msg='embodies exactly one italic element with valid content')

  def test_strikethrough(self):
    strikethroughs = self.root.findall('body/p/s')
    self.assertTrue(all([ len(strikethroughs) == 1, xml.innerText(strikethroughs[0]) == 's element' ]),
        msg='embodies exactly one italic element with valid content')

  def test_upsilon(self):
    self.assertEqual(len(self.root.findall('body/*')), 3,
        msg='embodies no redundant elements')

if __name__ == '__main__':
  main(failfast=True)

# vim: set expandtab shiftwidth=2:
