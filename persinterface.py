from persio import iohandler as ioh
import os


class Persinterface:

    def convert(self):
        filename = raw_input("File to convert (default input_data.root)? \n")
        # if filename == '' will use default
        filename = filename or 'input_data.root'
        if os.path.isfile(filename):
            self.ioh_obj = ioh.IOHandler(filename)
            self.ioh_obj.root2xml()
            print "Successfully converted file", filename
        else:
            print 'ROOT file "' + filename + '" does not exist'

    def load(self):
        filename = raw_input(
            "File to load into memory (default input_data.xml)? \n")
        filename = filename or 'input_data.xml'
        if os.path.isfile(filename):
            try:
                self.ioh_obj
            except:
                self.ioh_obj = ioh.IOHandler()
            self.ioh_obj.xml2mem(filename)
            self.loaded = True
            print "Successfully loaded file\n", filename
        else:
            print 'XML file "' + filename + '" does not exist\n'
        pass

    def exit(self):
        exit(0)

    io_functions = {'1': ('Convert ROOT file to XML', convert),
                    '2': ('Load XML file', load),
                    '3': ('Exit', exit)}

    def __init__(self):
        self.loaded = False
        self.firstlaunch = True
        pass

    def welcome_message(self):
        if self.firstlaunch:
            print "\n"
            print "Welcome to the Persistance Engine 2014."
            print "Choose a number corresponding to what you would like to do:"
            self.firstlaunch = False
        else:
            print "\n"
            print "Choose action"

    def run(self):
        if not self.loaded:
            self.welcome_message()
            for key in sorted(self.io_functions.keys()):
                print key, ':', self.io_functions[key][0]
            cmd = raw_input()
            if cmd in self.io_functions.keys():
                self.io_functions[cmd][1](self)
        else:
            print "What type of analysis would you like to perform?"
            self.loaded = False
            pass
