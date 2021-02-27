#!/usr/bin/env python3
#
# SWA6MANU
# https://codeboard.io/projects/220621
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
    self.assertTrue(all([ len(titles) == 1, xml.innerText(titles[0]) == 'SWA6MANU' ]),
        msg='embodies exactly one title with valid content')

  def test_table(self):
    self.assertEqual(len(self.root.findall('body/table')), 1,
	msg='embodies exactly one table element')

  def test_thead(self):
    self.assertEqual(list(map(xml.innerText, self.root.findall('body/table/thead/tr/th'))), [
      'Date',
      'Details',
      'Folio',
      'Goods (£)',
      'VAT (£)',
      'Total (£)'
     ],	msg='embodies exactly six table headings with valid content')

  def test_tbody(self):
    self.assertEqual(len(self.root.findall('body/table/tbody/tr')), 3,
        msg='embodies exactly three rows in table body')

  def test_td(self):
    self.assertEqual(list(map(xml.innerText, self.root.findall('body/table/tbody/tr/td'))), [
      'Jan 15',
      'Jarvis & Sons',
      'PL8',
      '32.00',
      '5.60',
      '37.60',
      'Jan 26',
      'K Howard',
      'PL17',
      '100.00',
      '17.50',
      '117.50',
      None,
      None,
      None,
      '132.00',
      '23.10',
      '155.10'
    ], msg='embodies exactly eighteen table cells with valid content')

if __name__ == '__main__':
  main(failfast=True)

# vim: set expandtab shiftwidth=2:
