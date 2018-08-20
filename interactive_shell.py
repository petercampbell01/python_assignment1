from cmd import Cmd
import command_line
__author__ = "Peter Campbell"
__copyright__ = "Copyright 2018,BCPR301 Class Assignment 1"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Peter Campbell"
__email__ = "peter@intrepid-adventure.com"
__status__ = "Development"



class InteractiveShell(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.command = command_line.CommandLine()
        print('Welcome to the Python UML creator')
        self.command = command_line.CommandLine()
        self.prompt = ">>> "
        self.cmdloop('Starting prompt...\n'
            'Type "help" for commands')


    def do_validate(self, args):
        '''
        Validates single and multiple files as executable python code.
        Command:
        validate [filenames]
        Author: Peter
        '''
        self.command.validate_code(args)

    def do_make_uml(self, filenames):
        self.command.create_class_diagram()

    def do_save_to_csv(self, params = 'plants.py output.csv'):
        '''
        Saves specified file to csv.
        Command:
        save_to_csv [input_file] [output_file]
        Author: Peter
        '''
        self.command.create_csv(params)

    def do_load_csv_for_uml(self, params = 'output.csv'):
        '''
        Loads csv file and creates UML diagram
        Command:
        load_csv_for_uml [file.csv]
        Author: Peter
        '''
        args = params.split(' ')
        print(args)
        if len(args) >= 1:
            input_file = args[0]
        if input_file.endswith('.csv'):
            self.command.load_csv_for_uml(input_file)

    def do_pickle_file(self, filename = 'plants.py'):
        '''
        Load modules from single file and save them using pickle
        Author: Peter

        Command:
        pickle_modules [filename.py]
        '''
        self.command.pickle_module(filename)

    def do_load_pickle_for_uml(self, params = None):
        '''
        Loads previously saved module using pickle
        Author: Peter
        
        Command:
        load_pickle_for_uml
        '''
        self.command.pickle_to_uml()

    def do_quit(self, other):
        '''
        Quits programme.
        Author: Peter
        '''
        print("Goodbye ......")
        return True