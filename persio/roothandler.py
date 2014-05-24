""" This module combines functions used for interacting with ROOT files"""
# pylint: disable=E0611
# pylint: disable=E1101
from ROOT import gDirectory, gPad, gROOT, TGraphErrors, TFile
import numpy as np


def getkeynames(self):
    """
    Gets all keys from a directory in a ROOT TFile.
    Returns as list of strings. This is an extension
    to the TGraphErrors class.
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
    num = graph.GetN()
    for function in functions:
        column = function()
        column.SetSize(num)
        npcolumn = np.array(column, copy=True)  # potentially unused
        output.append(npcolumn)
    output = np.array(output)
    return (output.T, num)


def openroot(name):
    """ Open a ROOT file, return keynames and handle to file. """
    TFile.getkeynames = getkeynames
    myfile = TFile.Open(name)
    if myfile:
        return myfile, myfile.getkeynames()
    else:
        return myfile, None


def main():
    """ Testing procedure: plot all graphs in a ROOT file. """
    TFile.getkeynames = getkeynames
    myfile = TFile('input_data.root')
    gROOT.SetBatch(True)
    for name in myfile.getkeynames():
        graph = myfile.Get(name)
        if type(graph) is not TGraphErrors:
            continue
        graph.Draw()
        gPad.SaveAs("images/" + name + '.png')
        gPad.Clear()

if __name__ == '__main__':
    main()
