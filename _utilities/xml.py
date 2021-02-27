#!/usr/bin/env python3
#
# xml.py
# XML Utilities
#
# Ashen Gunaratne
# mail@ashenm.ml
#

def innerText(element):

  if not element.text:
    return element.text

  return ' '.join(element.text.split())

# vim: set expandtab shiftwidth=2:
