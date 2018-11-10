#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from LoadImages import Image
from Controller import Controller
from USegmentation import dice_coef_loss, load_test_data, preprocess
from _ast import Assert
from _pytest.outcomes import fail
from statsmodels.sandbox.distributions.sppatch import expect
from bokeh.util.tests.test_serialization import expected
from Cython.Compiler.Errors import message


class TestSegmentation(unittest.TestCase):

    # Test for the dice_coef_loss receive an strings instead of ints

    def testDice_coef_loss(self):
        self.assertRaises(TypeError, dice_coef_loss('test', 'test2'))

    # Test for the Load_test_data receive an int instead of a str

    def testLoad_test_data(self):
        self.assertRaises(TypeError, load_test_data(1031))

    # Test for the preprocess receive a str instead of a list

    def testPreprocess(self):
        self.assertRaises(TypeError, preprocess('test'))

    # Test for the Load_test_data receive an incorrect path

    def testLoad_test_data_Wrong_Path(self):
        self.assertRaises(TypeError,
                          load_test_data('Celular_Division\Source'))


if __name__ == '__main__':
    unittest.main()  # run all tests