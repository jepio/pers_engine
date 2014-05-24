""" This module combines functions used for interacting with XML files"""
import xml.etree.ElementTree as ET


def createindex(keynames):
    """
    Generate an XML tree, together with an
    index with all key names.
    Returns the XML tree reference.
    """
    indexstring = ' '.join(keynames)
    data = ET.Element("data")
    index = ET.SubElement(data, "index")
    index.text = indexstring
    return data


def createpoint(point, pointtuple):
    """
    Create a point entry in the graph entry.
    Pass point object and a tuple of values
    with errors.
    """
    xval, yval, xerr, yerr = pointtuple
    value = ET.SubElement(point, "x")
    value.text = str(xval)
    value = ET.SubElement(point, "y")
    value.text = str(yval)
    value = ET.SubElement(point, "xerr")
    value.text = str(xerr)
    value = ET.SubElement(point, "yerr")
    value.text = str(yerr)


def creategraph(xmlelement, graph_data, name, num):
    """
    Create a graph entry in the XML tree.
    Pass the mother element, an array of
    graph data, the graph name and the
    number of points.
    """
    graph = ET.SubElement(xmlelement, "graph")
    graph.set("name", name)
    graph.set("total", str(num))
    for i in xrange(num):
        point = ET.SubElement(graph, "point")
        point.set("number", str(i))
        pointtuple = graph_data[i]
        createpoint(point, pointtuple)


def writexml(xmlelement, name):
    """
    Write the XML tree to disk.
    """
    tree = ET.ElementTree(xmlelement)
    tree.write(name)
