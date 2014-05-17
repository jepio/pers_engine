#!/usr/bin/env python2

from ROOT import gDirectory, gPad, gROOT, TGraphErrors, TFile

def GetKeyNames(self, dir=""):
	"""
	Gets all keys from a directory in a ROOT TFile.
	Returns a list of strings.
	"""
	self.cd(dir)
	return [key.GetName() for key in gDirectory.GetListOfKeys()]

TFile.GetKeyNames = GetKeyNames

myfile = TFile('input_data.root')
gROOT.SetBatch(True)

for name in myfile.GetKeyNames():
	graph = myfile.Get(name)
	if type(graph) is not TGraphErrors:
		continue
	graph.Draw()
	gPad.SaveAs(name + '.png')
	gPad.Clear()
