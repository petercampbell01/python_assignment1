import controller
import sys

class CommandLine():

    def __init__(self):
        self.control = controller.Controller()

    def create_class_diagram(self, files):
        if self.control.create_class_diagram(files) == True:
            print('UML class diagram successfully created for {}'.format(files))

    def create_csv(self, infiles, outfile):
        if self.control.create_csv(infiles, outfile) == True:
            print('{} successfully created saved as {}'.format(infiles, outfile))

    def load_csv_for_uml(self, file):
        if self.control.load_csv_for_uml(file) == True:
            print("UML class diagram successfully created from {}".format(file))
        else:
            print("UML class diagram could not be created from {}".format(file))

    def validate_code(self, files):
        valid_files = self.control.validate_code(files)
        if valid_files != False:
            print('The following files have been validated: {}'.format(valid_files))
        else:
            print('Unable to validate files: {}'.format(files))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("USAGE: " + sys.argv[0] + " <pythonfiles>")
    #else:
    #    initiate_python_parser(sys.argv[1:])
    #files = ['plants.py']
    files = ['linkedlist.py']
    file = files[0]
    #csv_file = 'plants.csv'
    csv_file = 'linkedlist.csv'
    
    command = CommandLine()
    command.validate_code(files)
    command.create_class_diagram(files)
    command.create_csv(files, csv_file)
    command.load_csv_for_uml(csv_file)

