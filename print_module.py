#Output basic class information to screen

class Print_class:
	
	def print_module(self, modules):
		for (name, module) in modules.items():
			for c in module:
				print('Class: {}'.format(c.name) )
				for attr in c.attributes:
					print('	Attributes: '.format(attr.name))
				for func in c.functions:
					print('	Methods: {}'.format(func.name))
	