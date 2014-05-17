import roothandler as rh
import xmlhandler as xh
from ROOT import TGraphErrors


class IOHandler:

    def __init__(self, filename='input_data.root'):
        """
        Initialize the IOHandler with a filename to read from.
        Will define the output file as filename with the extension
        '.xml'.
        """
        self.input = filename
        self.output = filename.split('.')[0] + '.xml'

    def root2xml(self):
        """
        Reads a ROOT file and outputs all TGraphErrors
        objects into a XML file.
        """
        rootfile, keynames = rh.openroot(self.input)
        xmlfile = xh.createindex(keynames)
        for graphname in keynames:
            graph = rootfile.Get(graphname)
            if type(graph) is not TGraphErrors:
                continue
            array, number = rh.graphtonp(graph)
            xh.creategraph(xmlfile, array, graphname, number)
        xh.writexml(xmlfile, self.output)


"""
possible ways of finding:
indexing root[1][1]
root.findall("./graph/point/[@number='12']")
root.findall(".//point[@number='12']")
"""
