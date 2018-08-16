import py_compile

class CodeValidator:
    """
    Class to validate files before parsing
    Author: Peter
    >>> validate = CodeValidator()
    >>> result = validate.validate_files(['plants.py','LinkedListNode.py'])
    plants.py successfully validated
    LinkedListNode.py successfully validated
    >>> len(result)
    2
    >>> result = validate.validate_file('plants.py')
    plants.py successfully validated
    """

    def __init__(self):
        pass

    def validate_files(self, filename_list):
        validated_files = []
        for filename in filename_list:
            if self.validate_file(filename) == True:
                validated_files.append(filename)
        return validated_files
        

    def validate_file(self, filename):
        try:
            py_compile.compile(filename)
            print('{} successfully validated'.format(filename))
            return True
        except py_compile.PyCompileError as err :
            print('{} does not validate. Exception {}'.format(filename, err))
            return False
        except FileNotFoundError as err:
            print('{} cannot be found. Unable to validate file'.format(filename))
            return False
        except:
            print('Unknown exception. Could not validate file: {}. Please check that information has been correctly provided and that file is present in specified directory'.format(filename))
            return False



if __name__ =='__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)
