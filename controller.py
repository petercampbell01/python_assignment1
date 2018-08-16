import model
import uml_output as UMLout
import print_module as pm

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



