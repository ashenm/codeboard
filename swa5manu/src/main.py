#!/usr/bin/env python3
#
# SWA5MANU
# https://codeboard.io/projects/220600
# main.py
#
# Ashen Gunaratne
# mail@ashenm.ml
#

from os.path import dirname, join, realpath

def main():

  with open(join(dirname(realpath(__file__)), 'index.html'), mode='r') as stream:
    print(*stream.readlines())

if __name__ == '__main__':
  main()

# vim: set expandtab shiftwidth=2:
