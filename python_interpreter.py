# Takes input form the command line and initiates the controller 
# passing command line input to the controller which then uses
# the information to initiate the model which parses the require file/files

import sys
import python_controller as pc

def initiate_python_parser(command_line_args):
	controll = pc.Controller()
	controll.run_parser(command_line_args)
	

if __name__ == '__main__' :
   # USAGE: python_parser.py <filename or * for all>.py
    # FOR OUTPUTTING DOT: | dot -T png -o output.png

    if len(sys.argv) == 1:
        print("USAGE: " + sys.argv[0] + " <pythonfiles>")
    else:
        #print("STARTING PROCESSING")
        initiate_python_parser(sys.argv[1:])
        #(sys.stdout)
