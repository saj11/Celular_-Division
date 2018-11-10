import cv2

## @package Image
# Documentation for the module Image
#
#  More details.

# Documentation for the Image Class
#
#  More details.
class Image:
    ## Variable of the image's route.
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param name The image name to be load.
    def __init__(self, path, name = "\\imagen"):
        self._path = path
        print("load image")
        print(name)
        try:
            print("IM: "+self._path+name)
            self._img = cv2.imread(self._path+name)
            self._name = name
        except:
            self._img = None
            assert("Image not found.")
    
    ## Method that shows the image.
    #  @param self The object pointer.
    def show(self):
        cv2.imshow(self._name, self._img)
    
    ## Method that shows the image.
    #  @param path The path where is the image.
    @property
    def path(self):
        return self._path
    
    @property
    def name(self):
        return self._name


#Unit Test
# cantidad_imagenes = 3
# lista_imagenes = []
# 
# for i in range(cantidad_imagenes):
#     nombre = "imagen{}.png".format(i+1)
#     imagen = Image(nombre)
#     lista_imagenes.append(imagen)
# 
# for img in lista_imagenes:
#     print(img._name)
#     img.show()
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()