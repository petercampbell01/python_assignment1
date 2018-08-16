import controller
import sys

class CommandLine():

    def __init__(self):
        self.control = controller.Controller()

    def create_class_diagram(self, files):
        if self.control.create_class_diagram(files) == True:
            print('UML class diagram successfully created for {}'.format(files))





if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("USAGE: " + sys.argv[0] + " <pythonfiles>")
    #else:
    #    initiate_python_parser(sys.argv[1:])
    files = ['plants.py']
    command = CommandLine()
    command.create_class_diagram(files)
