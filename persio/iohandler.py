""" Module defines the IOHandler class for interacting with files. """
import roothandler as rh
import xmlhandler as xh


class IOHandler(object):

    """
    Class for interacting with ROOT/XML files, esp. converintg between them.
    """

    def __init__(self, filename='input_data.root'):
        """
        Initialize the IOHandler with a filename to read from.
        Will define the output file as filename with the extension
        '.xml'.
        """
        self.input = filename
        self.output = filename.split('.')[0] + '.xml'
        self.converted = False
        self.loaded = False

    def root2xml(self):
        """
        Reads a ROOT file and outputs all TGraphErrors
        objects into a XML file.
        Returns True or False depending on success/failure.
        """
        rootfile, keynames = rh.openroot(self.input)
        if rootfile:
            xmlfile = xh.createindex(keynames)
            keynames_copy = keynames[:]

            for graphname in keynames_copy:
                graph = rootfile.Get(graphname)
                if type(graph) is not rh.TGraphErrors:
    #                print "Removed object: ", graph
                    keynames.remove(graphname)
                    continue
                array, number = rh.graphtonp(graph)
                xh.creategraph(xmlfile, array, graphname, number)

            index = xmlfile.find("index")
            keynames.sort()
            index.text = ' '.join(keynames)
            xh.writexml(xmlfile, self.output)
            self.converted = True
            return True
        else:
            print "Specified file is not a valid ROOT file"
            return False

    def xml2mem(self, xmlfilename=None):
        """
        Loads either xmlfilename or the initialized output file into memory.
        Defines references to:
            xml tree,
            xml root,
            xml index
        and toggles a switch so the class knows it has something loaded.
        Returns True or False depending on success/failure.
        """
        if self.converted:
            xmlfilename = xmlfilename or self.output
        try:
            self.tree = xh.ET.parse(xmlfilename)
            self.root = self.tree.getroot()
            self.index = self.root[0].text.split()
            self.loaded = True
            return True
        except SyntaxError:
            print "File is not a valid XML file."
            self.loaded = False
            return False

    def xmlindex(self):
        """
        Returns the index of a loaded xml file.
        """
        if self.loaded:
            return self.index
        else:
            print 'XML file not loaded'

    def memgrabgraph(self, graphname):
        """
        Grabs a graph called graphname from the xml file. Returns a tuple of:
            x - x points
            y - y points
            xe - error bars on x points
            ye - error bars on y points
        """
        if self.loaded:
            graphdata = self.root.find("graph[@name='{0}']".format(graphname))
            graphdata = xh.ET.tostringlist(graphdata, method="text")
            graphdata = [float(val) for val in graphdata]
            (xval, yval, xerr, yerr) = (graphdata[::4], graphdata[1::4],
                                        graphdata[2::4], graphdata[3::4])
        return (xval, yval, xerr, yerr)


"""
possible ways of finding:
indexing root[1][1]
root.findall("./graph/point/[@number='12']")
root.findall(".//point[@number='12']")
"""
