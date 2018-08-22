import controller

__author__ = "Peter Campbell"
__copyright__ = "Copyright 2018,BCPR301 Class Assignment 1"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Peter Campbell"
__email__ = "peter@intrepid-adventure.com"
__status__ = "Development"


class CommandLine():

    def __init__(self):
        self.control = controller.Controller()

    def create_class_diagram(self, files):
        if self.control.create_class_diagram(files) is True:
            print('UML class diagram successfully '
                  'created for {}'.format(files))

    def create_csv(self, params):
        infiles = []
        args = params.split(' ')
        if len(args) >= 1:
            infiles.append(args[0])
            outfile = 'output.csv'
        if len(args) >= 2:
            outfile = args[1]
        if infiles[0].endswith('.py'):
            if self.control.create_csv(infiles, outfile) is True:
                print('{} successfully created saved as '
                      '{}'.format(infiles, outfile))
                return True
            else:
                return False
        else:
            return False

    def load_csv_for_uml(self, file='output.csv'):
        if self.control.load_csv_for_uml(file) is True:
            print("UML class diagram successfully "
                  "created from {}".format(file))
        else:
            print("UML class diagram could not be "
                  "created from {}".format(file))

    def validate_code(self, filenames):
        print("Validating code ...")
        files = []
        if type(filenames) == str:
            files.append(filenames)
        elif type(filenames) == list:
            files = filenames
        valid_files = self.control.validate_code(files)
        if valid_files is not False:
            print('The following files have been '
                  'validated: {}'.format(valid_files))
            return True
        else:
            print('Unable to validate files: {}'.format(files))

    def pickle_module(self, filename):
        if self.control.pickle_modules(filename) is True:
            print('{} successfully pickled'.format(filename))
            return True
        else:
            print('Unable to pickle {}'.format(filename))
            return False

    def pickle_to_uml(self):
        if self.control.pickle_to_uml() is True:
            print('UML successfully created from pickle')
        else:
            print('Was unable to create UML from pickle, '
                  'have you pickled anything lately?')
