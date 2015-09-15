#!/usr/bin/python

import data_structures

test_list = data_structures.LinkedList()

string1 = "this string"
string2 = "another string"
string3 = "the final string"
int1 = 674

print(test_list.size())

test_list.insert(string1)
test_list.insert(string2)
test_list.insert(string3)
test_list.insert(int1)

print(test_list.size())
test_list.print_list()
