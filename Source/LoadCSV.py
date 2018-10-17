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
    _route = "/Users/joshsalazar/Github/Celular_Division/POC/Others/csv/"
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param name The CSV name to be load.
    def __init__(self, name = "CSV"):
        try:
            self._csv_file = pandas.read_csv(self._route+name)
            self._name = name
        except :
            self._csv_file = None
            assert("CSV not found.")
    
    ## Method that shows the CSV.
    #  @param self The object pointer.
    def show(self):
        print(type(self._csv_file))
    
    ## Method that shows the csv.
    #  @param route The route where is the csv.
    def set_route(self, route):
        self._route = route


# cantidad_csv = 3
# lista_csv = []
# 
# for i in range(cantidad_csv):
#     nombre = "csv{}.csv".format(i+1)
#     csv = CSV(nombre)
#     lista_csv.append(csv)
#   
# for csv_example in lista_csv:
#     print(csv_example.__dict__)
#     csv.show()
#     print("-"*50)