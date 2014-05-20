import roothandler as rh
import xmlhandler as xh


class IOHandler:

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
        """
        rootfile, keynames = rh.openroot(self.input)
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

    def xml2mem(self, xmlfilename=None):
        if self.converted:
            xmlfilename = xmlfilename or self.output
        self.tree = xh.ET.parse(xmlfilename)
        self.root = self.tree.getroot()
        self.index = self.root[0].text.split()
        self.loaded = True

    def xmlindex(self):
        if self.loaded:
            return self.index
        else:
            print 'XML file not loaded'

    def memgrabgraph(self, graphname):
        if self.loaded:
            graphdata = self.root.find("graph[@name='{0}']".format(graphname))
            graphdata = xh.ET.tostringlist(graphdata, method="text")
            (x, y, xe, ye) = (graphdata[::4], graphdata[1::4],
                              graphdata[2::4], graphdata[3::4])
        return (x, y, xe, ye)


"""
possible ways of finding:
indexing root[1][1]
root.findall("./graph/point/[@number='12']")
root.findall(".//point[@number='12']")
"""
