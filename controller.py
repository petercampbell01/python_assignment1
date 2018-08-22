import os
import model
import uml_output as UMLout
import print_module as pm
import csv_plugin as csv
import python_code_validator as validator
import pickle_modules

__author__ = "Peter Campbell"
__copyright__ = "Copyright 2018,BCPR301 Class Assignment 1"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Peter Campbell"
__email__ = "peter@intrepid-adventure.com"
__status__ = "Development"


class Controller:

    def __init__(self):
        pass

    def run_parser(self, filenames):
        processor = model.FileProcessor()
        processor.process_files(filenames)
        self.extracted_modules = processor.get_modules()
        return self.extracted_modules

    def create_class_diagram(self, filenames):
        modules = self.run_parser(filenames)
        newUML = UMLout.MakeUML(False, False)
        return newUML.create_class_diagram(modules)

    def create_csv(self, in_filename, out_file='class_data.csv'):
        if type(in_filename) != list:
            temp_filename = in_filename
            in_filename = []
            in_filename.append(temp_filename)
        modules = self.run_parser(in_filename)
        csvhandler = csv.CSV_handler()
        if csvhandler.write_csv_file(modules, out_file) is True:
            return True
        else:
            return False

    def load_csv_for_uml(self, input_file='class_data.csv'):
        if os.path.isfile(input_file) is True:
            csvloader = csv.CSV_handler()
            module = csvloader.open_file(input_file)
            if module is not False:
                makediagram = UMLout.MakeUML(True, True)
                return makediagram.create_class_diagram(module)
            else:
                return False

    def validate_code(self, files):
        validate = validator.CodeValidator()
        return validate.validate_files(files)

    def pickle_modules(self, filename='plants.py'):
        file = [filename]
        parser = model.FileProcessor()
        parser.process_files(file)
        modules = parser.get_modules()
        pickler = pickle_modules.PickleModules()
        return pickler.save(modules)

    def load_pickle(self):
        pickler = pickle_modules.PickleModules()
        return pickler.load()

    def module_to_uml(self, module):
        makediagram = UMLout.MakeUML(True, True)
        return makediagram.create_class_diagram(module)

    def pickle_to_uml(self):
        module = self.load_pickle()
        return self.module_to_uml(module)
