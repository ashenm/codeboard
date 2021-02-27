#!/usr/bin/env python3
#
# SWA3MANU
# https://codeboard.io/projects/220592
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
    self.assertTrue(all([ len(titles) == 1, xml.innerText(titles[0]) == 'SWA3MANU' ]),
        msg='embodies exactly one title element with valid content')

  def test_image(self):
    images = self.root.findall('body/img[@alt][@src]')
    self.assertTrue(all([ len(images) == 1, images[0].get('src') == 'https://mdn.github.io/beginner-html-site-scripted/images/firefox-icon.png' ]),
        msg='embodies exactly one image element with valid alternate text and image URI')

  def test_paragraph(self):
    paragraphs = self.root.findall('body/p')
    self.assertTrue(all([ len(paragraphs) == 1, xml.innerText(paragraphs[0]) == 'A web browser is an application software that facilitates at minimum retrieval and interpretation of a web resource such as a webpage.' ]),
        msg='embodies exactly one paragraph with valid content')

  def test_upsilon(self):
    body = list(map(lambda element: element.tag, self.root.findall('body/*')))
    self.assertTrue(all([ len(body) == 3, body == [ 'h1', 'img', 'p' ] ]),
        msg='embodies elements in exact order without redundant elements')

if __name__ == '__main__':
  main(failfast=True)

# vim: set expandtab shiftwidth=2:
