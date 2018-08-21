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
    _route = "../Others/"
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param name The image name to be load.
    def __init__(self, name = "imagen"):
        try:
            self._img = cv2.imread(self._route+name)
            self._name = name
        except:
            assert("Image not found.")
    
    ## Method that shows the image.
    #  @param self The object pointer.
    def show(self):
        cv2.imshow(self._name, self._img)
    
    ## Method that shows the image.
    #  @param route The route where is the image.
    def set_route(self, route):
        self._route = route


cantidad_imagenes = 3
lista_imagenes = []

for i in range(cantidad_imagenes):
    nombre = "imagen{}.png".format(i+1)
    imagen = Image(nombre)
    lista_imagenes.append(imagen)

for img in lista_imagenes:
    img.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()