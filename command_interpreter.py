import sys
import command_line
import interactive_shell

class Interpreter:

    def __init__(self, args):
        self.command = command_line.CommandLine()
        self.comm = None  #command given by user
        self.input_file = None
        self.output_file = 'output.csv'
        self.check_command_line(args)
        self.run_command()

    def check_command_line(self, args):
        '''
        command_line [command] -i [input] -o [output] 
        '''
        #print(args)
        self.comm = args[1]
        print('command', self.comm)
        index = 0
        for arg in args:
            if arg == '-i':
                self.input_file = args[index + 1]
            elif arg == '-o':
                self.output_file = args[index + 1]
            index += 1

    def run_command(self):
        '''
        Commands:
        help, file-uml, to-csv, csv-uml, pickle, pickle-uml, validate
        '''
        if self.comm == 'file-uml':
            self.command.create_class_diagram(self.input_file)
        elif self.comm == 'to-csv':
            params = self.input_file + ' ' + self.output_file
            self.command.create_csv(params)
        elif self.comm == 'csv-uml':
            self.command.load_csv_for_uml(self.output_file)






if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('For help using the command line write: command_interpreter.py -help')
        interactive_shell.InteractiveShell()
    else:
        # print(sys.argv)
        interpret = Interpreter(sys.argv)

 
def testRun():
   #    initiate_python_parser(sys.argv[1:])
    files = ['plants.py']
    #files = ['linkedlist.py']
    file = files[0]
    csv_file = 'plants.csv'
    #csv_file = 'linkedlist.csv'
    command = command_line.CommandLine()
    command.validate_code(files)
    command.create_class_diagram(files)
    args = files[0] + ' ' + csv_file
    command.create_csv(args)
    command.load_csv_for_uml(csv_file)