import os
import unittest
from LoadImages import Image
from Controller import Controller

class TestImage(unittest.TestCase):
    
    def setUp(self):
        self.image = Image("/Users/joshsalazar/Github/Celular_Division/Source/Others/images/","imagen3.png")
        self.controller = Controller()
        
    def testCasePath(self):
        default_path = "/Users/joshsalazar/Github/Celular_Division/Source/Others/images/"
        assert default_path == self.image.path, 'Wrong Path.'
    
    def testCaseTypeExtension(self):
        allow_type = ["PNG", "JPG"]
        name = self.image.name
        type = name[name.rfind(".")+1:].upper()
        assert type in allow_type, 'Wrong type. Expected: {}\
        ,{}. Get: {}'.format(allow_type[0], allow_type[1], type)
        
    def testCaseInformationLost(self, n=3):
        test_images = ["imagen1.png","imagen2.png","imagen3.png"]
        if n >= len(test_images):
            n = len(test_images)
        for i in range(n):
            self.controller.create_Image(test_images[i])
        print(self.controller.list_images)
        assert len(self.controller.list_images) == n, "An image(s) was lost."
        
    def testCaseNoImge(self, n=0):
        test_images = ["imagen1.png","imagen2.png","imagen3.png"]
        if n >= len(test_images):
            n = len(test_images)
        for i in range(n):
            self.controller.create_Image(test_images[i])
        
        assert len(self.controller.list_images) == n, "Method works correctly"
    
if __name__ == "__main__":
    unittest.main() # run all tests