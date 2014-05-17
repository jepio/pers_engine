from persio import iohandler


def main_old():
    keynames = ["A", "B"]
    graph_data1 = [(0, 0, 0, 1), (0, 1, 2, 3)]
    graph_data2 = [(2, 3, 0, 1), (0, 6, 2, 8)]
    graph_data = [graph_data1, graph_data2]
    name = "tree.xml"
    root = persxml.createindex(keynames)
    for i in xrange(2):
        persxml.creategraph(root, graph_data[i], keynames[i], 2)
    persxml.writexml(root, name)


def main():
    obj = iohandler.IOHandler()
    obj.root2xml()

if __name__ == '__main__':
    main()
