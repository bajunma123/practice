#! /usr/bin/python

from deffunc import get_information, write_into_file

get_information()
write_into_file('000000.txt')

get_information('add another string')
write_into_file('000001.txt')
