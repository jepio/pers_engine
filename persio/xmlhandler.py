import xml.etree.ElementTree as ET


def createindex(keynames):
    indexstring = ' '.join(keynames)
    data = ET.Element("data")
    index = ET.SubElement(data, "index")
    index.text = indexstring
    return data


def createpoint(point, num, pointtuple):
    x, y, xerr, yerr = pointtuple
    value = ET.SubElement(point, "x")
    value.text = str(x)
    value = ET.SubElement(point, "y")
    value.text = str(y)
    value = ET.SubElement(point, "xerr")
    value.text = str(xerr)
    value = ET.SubElement(point, "yerr")
    value.text = str(yerr)


def creategraph(xmlelement, graph_data, name, num):
    graph = ET.SubElement(xmlelement, "graph")
    graph.set("name", name)
    for i in xrange(num):
        point = ET.SubElement(graph, "point")
        point.set("number", str(i))
        pointtuple = graph_data[i]
        createpoint(point, i, pointtuple)


def writexml(xmlelement, name):
    tree = ET.ElementTree(xmlelement)
    tree.write(name)