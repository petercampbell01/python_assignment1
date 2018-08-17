import pickle

__author__ = "Peter Campbell"
__copyright__ = "Copyright 2018,BCPR301 Class Assignment 1"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Peter Campbell"
__email__ = "peter@intrepid-adventure.com"
__status__ = "Development"

class PickleModules:
    '''
    Class saves modules and loads them using pickle
    '''

    def __init(self):
        pass

    def save(self, modules):
        try:
            with open('data.pickle', 'wb') as f:
                pickle.dump(modules, f)
            return True
        except:
            return False
    
    def load(self):
        try:
            with open('data.pickle', 'rb') as f:
                loadedModules = pickle.load(f)
                return loadedModules
        except IOError:
            print("Cannot find pickle jar! Please check that you have previously saved your modules")
            return False
        except:
            print('An error has occurred. Please try again later')
            return False

if __name__ == '__main__':
    pickler = PickleModules()
    pickler.save(12345)
    loadedData = pickler.load()
    print(loadedData)



