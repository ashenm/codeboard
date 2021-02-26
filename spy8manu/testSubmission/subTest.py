#!/usr/bin/env python3
#
# SPY8MANU
# https://codeboard.io/projects/190730
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
    self.assertEqual(src.both_ends('Hello'), 'Helo',
        msg='translates "Hello" to "Helo"')
    self.assertEqual(src.both_ends('vxyz'), 'vxyz',
        msg='translates "vxyz" to "vxyz"')
    self.assertEqual(src.both_ends('spring'), 'spng',
        msg='translates "spring" to "spng"')

  def test_task2(self):
    self.assertEqual(src.spinal_case('hello world'), 'hello-world',
        msg='translates "hello world", to "hello-world"')
    self.assertEqual(src.spinal_case('the ferocious lion'), 'the-ferocious-lion',
        msg='translates "the ferocious lion" to "the-ferocious-lion"')
    self.assertEqual(src.spinal_case('Current split view'), 'Current-split-view',
        msg='translates "Current split view" to "Current-split-view"')
    self.assertEqual(src.spinal_case('humanity'), 'humanity',
        msg='translates "humanity" to "humanity"')

  def test_task3(self):
    self.assertEqual(src.mix_up('mix', 'pod'), 'pox mid',
        msg='translates "mix", "pod" to "pox mid"')
    self.assertEqual(src.mix_up('dog', 'dinner'), 'dig donner',
        msg='translates "dog", "dinner" to "dig donner"')
    self.assertEqual(src.mix_up('gnash', 'sport'), 'spash gnort',
        msg='translates "gnash", "sport" to "spash gnort"')
    self.assertEqual(src.mix_up('pezzy', 'firm'), 'fizzy perm',
        msg='translates "pezzy", "firm" to "fizzy perm"')

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
