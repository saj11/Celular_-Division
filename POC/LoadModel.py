import h5py
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
import numpy

route = "/Users/joshsalazar/Github/Celular_Division/POC/Others/csv/"

## @package Model
# Documentation for the module Model
# FrameWork; Keras
#  More details.

# Documentation for the CSV Class
#
#  More details.
class Model:
    ## Variable of the model's number.
    _number = 0
    ## The constructor.
    #  @param self The object pointer.
    def __init__(self):
        self._model = None
        self._dataset = None
        self._X = None
        self._Y = None
        self._scores = None
        self._number += 1
    
    ## Method that give the number of the model.
    #  @param self The object pointer.
    #  @return The number of the model
    @property
    def number(self):
        return self._number
    
    ## Method that load the database to be use
    #  @param self The object pointer.
    #  @param path Name of the database.
    def load_dataset(self, path):
        self._dataset = numpy.loadtxt(route+path, delimiter=",")
        self._X = self._dataset[:,0:8]
        self._Y = self._dataset[:,8]
        
    ## Method that create a simple neural network
    #  @param self The object pointer.
    def create_model(self):
        numpy.random.seed(7)
        
        self._model = Sequential()
        self._model.add(Dense(12, input_dim=8, activation='relu'))
        self._model.add(Dense(8, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))
    
    ## Method that train the NN
    #  @param self The object pointer.
    def train(self):
        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self._model.fit(self._X, self._Y, epochs=150, batch_size=10)
    
    ## Method that test the NN
    #  @param self The object pointer.
    def test(self):
        self._scores = self._model.evaluate(self._X, self._Y)
        print("\n%s: %.2f%%" % (self._model.metrics_names[1], self._scores[1]*100))
    
    ## Method that save the NN's model
    #  @param self The object pointer.
    def save_mod(self):
        self._model.save('../POC/Others/model/model{}.h5'.format(self._number))
    
    ## Method that load the NN's model
    #  @param self The object pointer.
    #  @param name The NN name.
    def load_mod(self, name):
        self._model = load_model(name)
    
#Unit Test    
# m = Model()
# '''m.load_dataset("pima-indians-diabetes.csv")
# m.create_model()
# m.train()
# m.test()
# m.save_mod()'''
# 
# m.load_mod("/Users/joshsalazar/Github/Celular_Division/POC/Others/model/model{}.h5".format(m.number))
# m.load_dataset("pima-indians-diabetes.csv")
# m.test()

