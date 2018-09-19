from PIL import Image

class Cleaner:
    
    def __init__(self, path):
        self.path = path
        
    def clean_exif(self, img):
        try:
            image = Image.open(self.path+img)
            image.save(self.path+img)
        except:
            raise("Can't clean the metadata.")
