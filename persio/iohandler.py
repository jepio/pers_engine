import roothandler as rh
import xmlhandler as xh


class IOHandler:

    def __init__(self, filename='input_data.root'):
        self.input = filename
        self.output = filename.split('.')[0] + '.xml'

    def root2xml(self):
        rootfile = rh.openroot(self.input)
        keynames = rootfile.getkeynames()
        xmlfile = xh.createindex(keynames)
        #for graphname in keynames:
        #	graph = rootfile.Get(graphname)

        xh.writexml(xmlfile, self.output)

