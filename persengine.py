#!/usr/bin/env python2
from persio import iohandler
import persinterface as ui


def main():
    obj = iohandler.IOHandler()
#    obj.root2xml()
    interface = ui.Persinterface()
    while True:
        interface.run()

if __name__ == '__main__':
    main()


"""
def main_old():
    keynames = ["A", "B"]
    graph_data1 = [(0, 0, 0, 1), (0, 1, 2, 3)]
    graph_data2 = [(2, 3, 0, 1), (0, 6, 2, 8)]
    graph_data = [graph_data1, graph_data2]
    name = "tree.xml"
    root = iohandler.xh.createindex(keynames)
    for i in xrange(2):
        iohandler.xh.creategraph(root, graph_data[i], keynames[i], 2)
    iohandler.xh.writexml(root, name)
"""
