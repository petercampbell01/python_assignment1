'''
Purpose is to save loaded classes to csv format and then be able
to recover them and put them in a format which can then be used
for creating a uml diagram.
'''

import csv
import sys
import model as model

__author__ = "Peter Campbell"
__copyright__ = "Copyright 2018,BCPR301 Class Assignment 1"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Peter Campbell"
__email__ = "peter@intrepid-adventure.com"
__status__ = "Development"


class CSV_handler:

    def __init__(self):
        # self.filename = name
        pass

    def open_file(self, filename='myclass.csv'):
        # Opens csv file and loads each line of the file into list
        # Then load_data_to_module for parsing
        result = []
        try:
            with open(filename) as File:
                reader = csv.reader(File)
                for row in reader:
                    result.append(row)
            modules = self.load_data_to_module(result)
            return modules
        except FileNotFoundError:
            print('File cannot be found. Please check path and '
                  'file name or check that file exists')
            return False
        except:
            print('An error has occurred. Could not load '
                  'information from csv file.')
            return False

    def load_data_to_module(self, module_list):
        # This is used to parse list and reconsruct the class structure
        # current version will only work with a single file. Extenstion
        # should be easy
        # Module is loaded into dictionary which can then be used by by
        # the uml output to generate UML diagram

        # NEED TO DEAL WITH VISIBILITY PROPERTY

        module_name = ''
        modules = dict()
        newClass = None
        for aline in module_list:
            if aline[0] == 'module':
                module_name = aline[1]
                modules[module_name] = list()
            elif aline[0] == 'class':
                if newClass is None:
                    newClass = model.ClassNode(aline[1].strip())
                else:
                    modules[module_name].append(newClass)
                    newClass = model.ClassNode(aline[1].strip())
            elif aline[0] == 'attributes':
                loop_counter = 1
                while loop_counter < len(aline):
                    newClass.add_attribute(aline[loop_counter].strip(), False)
                    loop_counter += 1
            elif aline[0] == 'methods':
                loop_counter = 1
                while loop_counter < len(aline):
                    newClass.add_function(aline[loop_counter].strip(),
                                          'params', False)
                    loop_counter += 1
            elif aline[0] == 'super_classes':
                pass
        modules[module_name].append(newClass)
        return modules

    def write_csv_file(self, modules, filename='myclass.csv'):
        # Writes module as received from model or from self.open_file
        # to specified csv file.
        output = ''
        for (name, module) in modules.items():
            output += 'module,{}\n'.format(name)
            for c in module:
                output += 'class,{}'.format(c.name)
                if len(c.attributes) > 0:
                    output += '\nattributes'
                for attr in c.attributes:
                    output += ',{}'.format(attr.name)
                if len(c.functions) > 0:
                    output += '\nmethods'
                for func in c.functions:
                    output += ',{}'.format(func.name)
                if c.super_classes is not None:
                    if len(c.super_classes) > 0:
                        output += '\nsuper_classes'
                        for super_class in c.super_classes:
                            output += ',{}'.format(super_class)
                output += '\n'
        try:
            with open(filename, "wt") as f:
                f.write(output)
            return True
        except IOError:
            print("Cannot write csv file. Try again another day")
            return False
        except PermissionError:
            print('You do not have appropriate permissions on '
                  'this system to save the file')
            return False
        except:
            print('The system encountered a problem here. '
                  'Please turn off your computer,')
            print('jump up and down three times, flap your arms '
                  'and quack like a duck and then try again.')
            return False


if __name__ == '__main__':
    csvhandler = CSV_handler()
    newmodule = csvhandler.open_file('plants.csv')
    # print(newmodule)
    # print('------------------------------')
    # doParse = model.FileProcessor()
    # filenames =["plants.py"]
    # outfile = filenames[0].replace('.py', '.csv')
    # doParse.process_files(filenames)
    # modules = doParse.get_modules()
    # print(modules)
    # csvhandler.write_csv_file(modules, outfile)
    # csvhandler.write_csv_file(newmodule, 'myclass.csv')

    import uml_output as uml
    makediagram = uml.MakeUML(True, True)
    # makediagram.create_class_diagram(newmodule)
