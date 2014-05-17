#import persio.roothandler
import persio.xmlhandler as xml

keynames = ["A", "B"]
graph_data1 = [(0, 0, 0, 1), (0, 1, 2, 3)]
graph_data2 = [(2, 3, 0, 1), (0, 6, 2, 8)]
graph_data = [graph_data1, graph_data2]
name = "tree.xml"

root = xml.createindex(keynames)

for i in xrange(2):
    xml.creategraph(root, graph_data[i], keynames[i],2)

xml.writexml(root, name)
