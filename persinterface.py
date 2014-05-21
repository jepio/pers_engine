from persio import iohandler as ioh
import os


def pretty_print(CL_output):
    """
    Borrowed from stackexchange.
    """
    columns = len(CL_output) // 30 + 2
    for i, val in enumerate(CL_output):
        CL_output[i] = '\033[1;31m{:2d}\033[1;m'.format(i) + ": " + val
    lines = ("".join(s.ljust(30) for s in CL_output[i:i + columns - 1]) + CL_output[i:i + columns][-1]
             for i in range(0, len(CL_output), columns))
#    if float(len(CL_output)) / columns != len(CL_output) // columns:
#        del CL_output[-1]
    return "\n".join(lines)


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

    def index(self):
        print pretty_print(self.ioh_obj.xmlindex())

    def plot(self):
        pass

    def trend(self):
        pass

    def back(self):
        self.loaded = False

    io_functions = {'1': ('Convert ROOT file to XML', convert),
                    '2': ('Load XML file and perform analysis', load),
                    '3': ('Exit', exit)}

    analysis_functions = {'1': ('Print graph index', index),
                          '2': ('Plot a graph', plot),
                          '3': ('Perform a trend analysis', trend),
                          '4': ('Return to I/O operations', back)}

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

    def select(self, array):
        self.welcome_message()
        for key in sorted(array.keys()):
            print key, ':', array[key][0]
        cmd = raw_input()
        if cmd in array.keys():
            array[cmd][1](self)

    def run(self):
        if not self.loaded:
            self.select(self.io_functions)
        else:
            self.select(self.analysis_functions)
            pass
