from persio import iohandler as ioh


class Persinterface:
	def convert(self):
		filename = raw_input("File to convert (default input_data.root) \n")
		filename = filename or 'input_data.root' # if filename == '' will use default
		self.ioh_obj = ioh.IOHandler(filename)
		self.ioh_obj.root2xml()
		print "Successfully converted file", filename
		pass

	def load(self):
		print 'load function'
		pass

	io_functions = { '1' : ('Convert ROOT file to XML', convert),
					 '2' : ('Load XML file', load) }


	def __init__(self):
		pass



	def welcome_message(self):
		print ""
		print "Welcome to the Persistance Engine 2014."
		print "Press a number corresponding to what you would like to do:"

	def run(self):
		self.welcome_message()
		for key in sorted(self.io_functions.keys()):
			print key,' ',self.io_functions[key][0]
		cmd = raw_input()
		self.io_functions[cmd][1](self)