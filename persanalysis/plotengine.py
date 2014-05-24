""" Module for plotting graphs to file """
import matplotlib.pyplot as plt


class PlotEngine(object):

    """ Class that performs saving of plots """

    def __init__(self, data_tuple, name):
        xval, yval, xerrors, yerrors = data_tuple
        self.output_name = name
        plt.errorbar(xval, yval, xerr=xerrors, yerr=yerrors)
        plt.title(name)
        self.labels()

    def save(self, extension):
        """ Save the plot with extension """
        name = self.output_name + "." + extension
        plt.savefig(name, bbox_inches="tight")
        plt.close()

    @staticmethod
    def labels(xlabel=r'temperature ($^\circ$C)',
               ylabel="current (mA)"):
        """ Label the axes """
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
