import os
import model
import uml_output as UMLout
import print_module as pm
import csv_plugin as csv
import python_code_validator as validator

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

    def create_csv(self, in_filename, out_file = 'class_data.csv'):
        if type(in_filename) != list:
            temp_filename = in_filename
            in_filename = []
            in_filename.append(temp_filename)
        modules = self.run_parser(in_filename)
        csvhandler = csv.CSV_handler()
        csvhandler.write_csv_file(modules, out_file)

    def load_csv_for_uml(self, input_file = 'class_data.csv'):
        if os.path.isfile(input_file) == True:
            csvloader = csv.CSV_handler()
            module = csvloader.open_file(input_file)
            if module != False:
                makediagram = UMLout.MakeUML(True, True)
                return makediagram.create_class_diagram(module)
            else:
                return False
    
    def validate_code(self, files):
        validate = validator.CodeValidator()
        return validate.validate_files(files)