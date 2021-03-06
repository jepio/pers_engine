""" The Persistency UI module, defines the Persinterface class, which offers
the user the command-line interface. """
from persio import iohandler as ioh
from persanalysis import plotengine as pe
from persanalysis import fitengine as fe
from persanalysis import trendengine as te
import sys
import os


def pretty_print(array):
    """
    Convert array to columns. Borrowed from stackexchange.

    Returns joined string.
    """
    cl_output = array[:]
    columns = len(cl_output) // 30 + 2
    for i, val in enumerate(cl_output):
        cl_output[i] = '{:2d}'.format(i) + ": " + val
    lines = ("".join(s.ljust(20) for s in cl_output[i:i + columns])
             for i in range(0, len(cl_output), columns))
    return "\n".join(lines)


class Persinterface(object):

    """
    The User Interface class, defines methods for the user to execute.
    To extend functionality, write an extra function and add to the function
    dictionaries.
    """

    def convert(self):
        """
        Convert file from ROOT to XML verbosely.
        Will default to input_data.root as the filename.
        """
        filename = raw_input("File to convert (default input_data.root)? \n")
        # if filename == '' will use default
        filename = filename or 'input_data.root'
        if os.path.isfile(filename):
            self.ioh_obj = ioh.IOHandler(filename)
            if self.ioh_obj.root2xml():
                print "Successfully converted file", filename
            else:
                print "Failed to convert file"
        else:
            print 'ROOT file "' + filename + '" does not exist'

    def load(self):
        """
        Load XML file into the engine verbosely.
        Will default to input_data.xml as the filename.
        """
        filename = raw_input(
            "File to load into memory (default input_data.xml)? \n")
        filename = filename or 'input_data.xml'
        if os.path.isfile(filename):
            try:
                self.ioh_obj
            except AttributeError:
                self.ioh_obj = ioh.IOHandler()
            self.loaded = self.ioh_obj.xml2mem(filename)
            if self.loaded:
                print "Successfully loaded file", filename
            else:
                print "Failed to load file"
        else:
            print 'XML file "' + filename + '" does not exist\n'

    def exit(self):
        """ Exit program. """
        sys.exit(0)

    def index(self):
        """ Print loaded XML objects index field. """
        print pretty_print(self.ioh_obj.xmlindex())

    @staticmethod
    def ask(question, dictionary, quiet=False):
        """
        Check whether answer to question is in dictionary.

        Returns logic value and dictonary value
        """
        print "Choose " + question
        if not quiet:
            for number in sorted(dictionary.keys()):
                opt = dictionary[number]
                types = [int, str]
                choice = opt if type(opt) in types else opt[0]
                print number, ':', choice

        answer = raw_input()
        if answer in dictionary.keys():
            return True, dictionary[answer]
        else:
            return False, None

    def plot(self):
        """ Plot graph from loaded XML file. """
        extensions = {'1': 'eps', '2': 'pdf', '3': 'png'}
        index_list = self.ioh_obj.xmlindex()
        last = len(index_list)
        graph_num = dict((str(i), i) for i in xrange(last))
        present, num = self.ask("graph number (valid: 0-" + str(last - 1)
                                + ")", graph_num, quiet=True)
        if present:
            present, ext = self.ask("file extension", extensions)
            if present:
                name = index_list[num]
                data = self.ioh_obj.memgrabgraph(name)
                plotter = pe.PlotEngine(data, name)
                print "File saved as", plotter.save(ext)
                plotter.close()
            else:
                print "Wrong extension, saving cancelled."
        else:
            print "The specified number is not valid."

    def trend(self):
        """ Perform trending analysis of current@point in time. """
        extensions = {'1': 'eps', '2': 'pdf', '3': 'png'}
        point_num = dict((str(i), i) for i in xrange(34 + 1))
        method = {'1': ('Point number', 1), '2': ('Closest temperature', 2)}
        num = None
        coord = None
        present, meth = self.ask("trending based on:", method)
        if present:
            if meth[1] == 1:
                present, num = self.ask("point number to trend (valid: 0-34)",
                                        point_num, quiet=True)
            elif meth[1] == 2:
                try:
                    coord = raw_input("Choose temperature (valid:"
                                      " -10.0 - 10.0) \n")
                    coord = float(coord)
                    present = True if coord ** 2 <= 100 else False
                except ValueError:
                    coord = None
                    present = False
            if present:
                present, ext = self.ask("file extension", extensions)
                if present:
                    trender = te.TrendEngine(self.ioh_obj, point_num=num,
                                             xcoord=coord)
                    print "File saved as", trender.save(ext)
                    trender.close()
                else:
                    print "Wrong extension, saving cancelled."
            else:
                print "The specified number is not valid."
        else:
            print "Wrong trending method."

    def fitting(self):
        """ Fit a curve to data """
        functions = {'1': ('Linear fit', "lin"),
                     '2': ('Exponential fit', "exp")}
        extensions = {'1': 'eps', '2': 'pdf', '3': 'png'}
        index_list = self.ioh_obj.xmlindex()
        last = len(index_list)
        graph_num = dict((str(i), i) for i in xrange(last))
        present, num = self.ask("graph number (valid: 0-" + str(last - 1)
                                + ")", graph_num, quiet=True)
        if present:
            name = index_list[num]
            data = self.ioh_obj.memgrabgraph(name)
            present, func = self.ask("function to fit", functions)
            if present:
                present, ext = self.ask("file extension", extensions)
                if present:
                    fitter = fe.FitEngine(data, name, func[1])
                    print "File saved as", fitter.save(ext)
                    fitter.close()
                else:
                    print "Wrong extension, saving cancelled."
            else:
                print "Wrong function input"
        else:
            print "The specified number is not valid"

    def back(self):
        """ Go back to I/O menu. """
        self.loaded = False

    io_functions = {'1': ('Convert ROOT file to XML', convert),
                    '2': ('Load XML file and perform analysis', load),
                    '3': ('Exit', exit)}

    analysis_functions = {'1': ('Print graph index', index),
                          '2': ('Plot a graph', plot),
                          '3': ('Perform curve fitting to a graph', fitting),
                          '4': ('Perform a trend analysis', trend),
                          '5': ('Return to I/O operations', back)}

    def __init__(self):
        self.loaded = False
        self.firstlaunch = True

    def welcome_message(self):
        """ Print the welcome message. """
        if self.firstlaunch:
            print ""
            print "Welcome to the Persistance Engine 2014."
            print ""
            print "Choose a number corresponding to what you would like to do:"
            self.firstlaunch = False
        else:
            print ""
            print "Choose action"

    def select(self, array):
        """ Select an action from array based on user input. """
        self.welcome_message()
        for key in sorted(array.keys()):
            print key, ':', array[key][0]
        cmd = raw_input()
        if cmd in array.keys():
            array[cmd][1](self)

    def run(self):
        """ Run the user interface. """
        if not self.loaded:
            self.select(self.io_functions)
        else:
            self.select(self.analysis_functions)
