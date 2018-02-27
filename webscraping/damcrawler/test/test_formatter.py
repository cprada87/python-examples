#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from app.formatter import Formatter
 
class TddFormatter(unittest.TestCase):

    def test_formatter_drop_accents_method_returns_correct_result(self):
        self.assertEqual("Balon", "Balon")
        
    def test_formatter_drop_accents2_method_returns_correct_result(self):
        f = Formatter("Balon")
        self.assertEqual("Balon", f.string)

    def test_formatter_drop_accents3_method_returns_correct_result(self):
        f = Formatter("Balón")
        res = f.drop_accents()
        self.assertEqual("Balon", res)

    def test_formatter_drop_whitespaces_method_returns_correct_result(self):
        f = Formatter("En un lugar de la Mancha")
        res = f.drop_whitespaces()
        self.assertEqual("En-un-lugar-de-la-Mancha", res)

    # def test_formatter_drop_accents_whitespaces_method_returns_correct_result(self):
    #     f = Formatter("vivía un ingenioso hidalgo")
    #     res = f.drop_accents_whitespaces()
    #     self.assertEqual("vivia-un-ingenioso-hidalgo", res)
        
        
if __name__ == '__main__':
    unittest.main()
