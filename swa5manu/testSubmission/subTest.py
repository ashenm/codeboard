#!/usr/bin/env python3
#
# SWA5MANU
# https://codeboard.io/projects/220600
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

    if not type(self.root) is ElementTree.ParseError:
      self.markup = ''.join(ElementTree.tostring(self.root, encoding='us-ascii')
          .decode(encoding='us-ascii').split())
    else:
       self.markup = ''

    super().__init__(*args, **kargs)

  def test_alpha(self):
    self.assertNotIsInstance(self.root, ElementTree.ParseError, msg=str(self.root))

  def test_beta(self):
    titles = self.root.findall('head/title')
    self.assertTrue(all([ len(titles) == 1, xml.innerText(titles[0]) == 'SWA5MANU' ]),
        msg='embodies exactly one title with valid content')

  def test_delta(self):
    self.assertRegex(self.markup, r'>2<sup>n</sup><',
	msg='embodies approximately formatted 2n expression')

  def test_gamma(self):
    self.assertRegex(self.markup, r'>2<sup>n</sup><',
	msg='embodies appropriately formatted 2n expression')

  def test_kappa(self):
    self.assertRegex(self.markup, r'>H<sub>2</sub>O<',
	msg='embodies appropriately formatted H20 expression')

  def test_nu(self):
    self.assertRegex(self.markup, r'>cos\(2&#952;\)=cos<sup>2</sup>&#952;-sin<sup>2</sup>&#952;<',
	msg='embodies appropriately formatted cos(2θ) expression')

  def test_mu(self):
    self.assertRegex(self.markup, r'>&#960;&#8776;3.14<',
	msg='embodies appropriately formatted π expression')

  def test_omicron(self):
    self.assertRegex(self.markup, r'><b>&#946;</b>=\(&#946;<sub>1</sub>,&#946;<sub>2</sub>,...,&#946;<sub>n</sub>\)<',
	msg='embodies appropriately formatted β expression')

if __name__ == '__main__':
  main(failfast=True)

# vim: set expandtab shiftwidth=2:
