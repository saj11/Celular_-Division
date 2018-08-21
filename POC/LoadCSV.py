import pandas

## @package CSV
# Documentation for the module CSV
#
#  More details.

# Documentation for the CSV Class
#
#  More details.
class CSV:
    ## Variable of the csv's route.
    _route = "../Others/"
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param name The CSV name to be load.
    def __init__(self, name = "CSV"):
        try:
            self._csv = pandas.read_csv(self._route+name)
            self._name = name
        except :
            assert("CSV not found.")
    
    ## Method that shows the CSV.
    #  @param self The object pointer.
    def show(self):
        print(self._csv)
    
    ## Method that shows the csv.
    #  @param route The route where is the csv.
    def set_route(self, route):
        self._route = route


cantidad_csv = 3
lista_csv = []

for i in range(cantidad_csv):
    nombre = "csv{}.csv".format(i+1)
    csv = CSV(nombre)
    lista_csv.append(csv)
  
for csv in lista_csv:
     csv.show()
     print("-"*50)