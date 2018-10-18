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
    
    
    def testLossfunction(self):
        #dice_coef_loss("y_true", "y_pred")
        #assert TypeError , "The function can receive strings"
        self.assertRaises(TypeError,dice_coef_loss(1.4, 12.4))

    def testLoad_test_data(self):
        self.assertRaises(TypeError,load_test_data("adafa"))

    def testPreprocess(self):
        self.assertRaises(TypeError,preprocess(10.0))
    
    





if __name__ == "__main__":
    unittest.main() # run all tests

