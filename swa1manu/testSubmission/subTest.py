#!/usr/bin/env python3
#
# SWA1MANU
# https://codeboard.io/projects/220011
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

  def test_title(self):
    titles = self.root.findall('head/title')
    self.assertTrue(all([ len(titles) == 1, xml.innerText(titles[0]) == 'SWA1MANU' ]),
        msg='embodies exaclty one title element with valid content')

  def test_h1(self):
    headers = self.root.findall('body/h1')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 1' ]),
        msg='embodies exaclty one h1 element with valid content')

  def test_h2(self):
    headers = self.root.findall('body/h2')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 2' ]),
        msg='embodies exaclty one h2 element with valid content')

  def test_h3(self):
    headers = self.root.findall('body/h3')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 3' ]),
        msg='embodies exaclty one h3 element with valid content')

  def test_h4(self):
    headers = self.root.findall('body/h4')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 4' ]),
        msg='embodies exaclty one h4 element with valid content')

  def test_h5(self):
    headers = self.root.findall('body/h5')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 5' ]),
        msg='embodies exaclty one h5 element with valid content')

  def test_h6(self):
    headers = self.root.findall('body/h6')
    self.assertTrue(all([ len(headers) == 1, xml.innerText(headers[0]) == 'heading level 6' ]),
        msg='embodies exaclty one h6 element with valid content')

  def test_redundant(self):
    self.assertTrue(all([ len(self.root.findall('body/*')), 6 ]),
        msg='embodies no redundant elements')

if __name__ == '__main__':
  main(failfast=True)

# vim: set expandtab shiftwidth=2:
