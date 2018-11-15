import os
from platform import system
import Cleaner
from LoadImages import Image
from LoadCSV import CSV
import USegmentation
import csv
from email._header_value_parser import _fold_as_ew


class Controller:
    _folder = ""
    
    def __init__(self):
        if(str(system()) == "Windows"):
            _folder = "\\Resources\images\\"
            self._folder_csv = "\\Resources\\csv\\"
        else:
            _folder = "/Resources/images/"
            self._folder_csv = "/Resources/csv/"
        #print(os.path.abspath(_folder))
        print("Controller")
        self._project_path = os.path.dirname(os.path.abspath(__file__))
        print(os.path.abspath(__file__))
        #print("PP: "+self._project_path)
        self._images_path = ""
        self._list_images = []
        
    def process_images(self):
        try:
            result = USegmentation.predict()
            try:
                self.create_csv(self._project_path + self._folder_csv, result)
            except:
                print("Error while creating the report")
        except:
            print("Error while processing the images")
        
    def create_csv(self, path, dict_to_write):
        with open(path + 'report.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Number of Cell', 'Center Position(X-Y)', 'Area'])
            for number_image,list_of_cells in dict_to_write.items():
                filewriter.writerow(['Image #{}'.format(number_image)])
                for cell in list_of_cells:
                    filewriter.writerow([cell[0], str(cell[1][0])+"-"+str(cell[1][1]), cell[2]])
        
    def create_folder(self):
        print(self._folder)
        self._images_path = self._project_path+"\\Resources\images\\"
        #print("IP: "+self._images_path)
        if not os.path.isdir(self._images_path):   #Search if there is a directory to save images uploaded
            print(os.mkdir(self._images_path))
            os.mkdir(self._images_path)
            print("Could create directory: {}.".format(target))
    
    def _list_files(self, folder):
        print(os.listdir(folder))
        return os.listdir(folder)
    
    def create_Image(self, img):
        image = Image(self._images_path, img)
        self._list_images.append(image)
    
    @property
    def images_path(self):
        return self._images_path
    
    @property
    def list_images(self):
        #return self._list_files(self._project_path+os.path.abspath(self._folder))
        return os.path.abspath(self._folder)
    
    @list_images.setter
    def list_images(self, list_images):
        self._list_images = list_images