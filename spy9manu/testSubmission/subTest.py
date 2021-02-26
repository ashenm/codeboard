#!/usr/bin/env python3
#
# SPY9MANU
# https://codeboard.io/projects/192547
# subTest.py
#
# Ashen Gunaratne
# mail@ashenm.ml
#

from io import StringIO
from unittest.mock import patch
from unittest import TestCase, main

import src.main as src

class subTest(TestCase):

  def test_task1(self):

    # disclosed tests
    self.assertEqual(src.fix_start('babble'), 'ba**le',
        msg='translates "babble" to "ba**le"')
    self.assertEqual(src.fix_start('aardvark'), 'a*rdv*rk',
        msg='translates "aardvark" to "a*rdv*rk"')
    self.assertEqual(src.fix_start('zippy fizzy'), 'zippy fi**y',
        msg='translates "zippy fizzy" to "zippy fi**y"')

    # hidden tests
    self.assertEqual(src.fix_start('google'), 'goo*le',
        msg='translates "google" to "goo*le"')
    self.assertEqual(src.fix_start('donut'), 'donut',
        msg='translates "donut" to "donut"')
    self.assertEqual(src.fix_start('iffen iise'), 'iffen **se',
        msg='translates "iffen iise" to "iffen **se"')

  def test_task2(self):

    # disclosed tests
    self.assertEqual(src.text_align('dabble', '='), '=====dabble====',
        msg='translates "dabble", "=" to "=====dabble===="')
    self.assertEqual(src.text_align('baffle', '*'), '*****baffle****',
        msg='translates "baffle", "*" to "*****baffle****"')
    self.assertEqual(src.text_align('dabble dibble baffle', ' '), 'dabble dibble baffle',
        msg='translates "dabble dibble baffle", " " to "dabble dibble baffle"')

    # hidden tests
    self.assertEqual(src.text_align('tableware', '-'), '---tableware---',
        msg='translates "tableware", "-" to "---tableware---"')
    self.assertEqual(src.text_align('abcdefghijklmnopqrst', ' '), 'abcdefghijklmnopqrst',
        msg='translates "abcdefghijklmnopqrst", " " to "abcdefghijklmnopqrst"')
    self.assertEqual(src.text_align('abcdefghijk', ' '), '  abcdefghijk  ',
        msg='translates "abcdefghijk", " " to "  abcdefghijk  "')

  def test_task3(self):

    # disclosed tests
    self.assertEqual(src.swap_case('swimingly'), 'SWIMINGLY',
        msg='translates "swimingly" to "SWIMINGLY"')
    self.assertEqual(src.swap_case('haIlIng'), 'HAiLiNG',
        msg='translates "haIlIng" to "HAiLiNG"')
    self.assertEqual(src.swap_case('Do'), 'dO',
        msg='translates "Do" to "dO"')

    # hidden tests
    self.assertEqual(src.swap_case('DONE'), 'done',
        msg='translates "DONE" to "done"')
    self.assertEqual(src.swap_case('FixtureS'), 'fIXTUREs',
        msg='translates "FixtureS" to "fIXTUREs"')
    self.assertEqual(src.swap_case('paint'), 'PAINT',
        msg='translates "paint" to "PAINT"')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
