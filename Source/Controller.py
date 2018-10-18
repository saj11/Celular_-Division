import os
from platform import system
import Cleaner
from LoadImages import Image
from LoadCSV import CSV
import USegmentation


class Controller:
    _folder = ""
    
    def __init__(self):
        if(str(system()) == "Windows"):
            _folder = "\\Resources\\images\\"
        else:
            _folder = "/Resources/images/"
        #print(os.path.abspath(_folder))
        self._project_path = os.path.dirname(os.path.abspath(__file__))
        #print("PP: "+self._project_path)
        self._images_path = ""
        self._list_images = []
        
    def process_images(self):
        try:
            USegmentation.predict()
        except:
            print("Error while processing the images")
        
    def create_folder(self):
        self._images_path = self._project_path+self._folder
        #print("IP: "+self._images_path)
        if not os.path.isdir(self._images_path):   #Search if there is a directory to save images uploaded
            os.mkdir(self._images_path)
            print("Could create directory: {}.".format(target))
    
    def _list_files(self, folder):
        return os.listdir(folder)
    
    def create_Image(self, img):
        image = Image(self._images_path, img)
        self._list_images.append(image)
    
    @property
    def images_path(self):
        return self._images_path
    
    @property
    def list_images(self):
        #print("voy por aqui suma de paths")
        #print(self._project_path)
        #word = os.path.abspath(self._folder)
        #print(word.split(':')[1])
        print (os.path.abspath(self._folder))
        return os.path.abspath(self._folder)
    
    @list_images.setter
    def list_images(self, list_images):
        self._list_images = list_images