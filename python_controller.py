import model
import umloutput as UMLout
import print_module as pm

class Controller:
	
	def __init__(self):
		pass
	
	def run_parser(self, filenames):
		# Initiate processor
		processor = model.FileProcessor()
		processor.process_files(filenames)
		extracted_modules = processor.get_modules()
		print_to_screen = pm.Print_class()
		print_to_screen.print_module(extracted_modules)
		#newUML = UMLout.MakeUML()
		#newUML.create_class_diagram(extracted_modules)
