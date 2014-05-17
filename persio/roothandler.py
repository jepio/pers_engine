from ROOT import gDirectory, gPad, gROOT, TGraphErrors, TFile
import numpy as np


def getkeynames(self):
    """
    Gets all keys from a directory in a ROOT TFile.
    Returns a list of strings.
    """
    self.cd()
    return [key.GetName() for key in gDirectory.GetListOfKeys()]


def graphtonp(graph):
    """
    Converts a TGraphErrors object into a numpy array
    that has columns: x, y, xerr, yerr.
    """
    output = []
    functions = (graph.GetX, graph.GetY, graph.GetEX, graph.GetEY)
    n = graph.GetN()
    for function in functions:
        column = function()
        column.SetSize(n)
        npcolumn = np.array(column, copy=True)
        output.append(column)
    output = np.array(output)
    return output.T

def openroot(name):
    TFile.getkeynames = getkeynames
    myfile = TFile(name)
    return myfile



# Testing procedure
def main():
    TFile.getkeynames = getkeynames
    myfile = TFile('input_data.root')
    gROOT.SetBatch(True)
    for name in myfile.getkeynames():
        graph = myfile.Get(name)
        if type(graph) is not TGraphErrors:
            continue
        graph.Draw()
        gPad.SaveAs(name + '.png')
        gPad.Clear()

if __name__ == '__main__':
    main()
