""" Module for plotting graphs to file """
import matplotlib.pyplot as plt
# import numpy as np


class PlotEngine(object):

    """ Class that performs saving of plots. """

    def __init__(self, data_tuple, name):
        xval, yval, xerrors, yerrors = data_tuple
        self.xval = xval
        self.yval = yval
        self.name = name
        plt.errorbar(xval, yval, xerr=xerrors, yerr=yerrors, marker=".",
                     linestyle="None")
        self.style()

    def save(self, extension):
        """ Save the plot with extension """
        name = self.name + "." + extension
        plt.savefig(name, bbox_inches="tight", dpi=96 * 2)
        plt.close()
        return name

    def style(self, xlabel=r'temperature ($^\circ$C)',
              ylabel="current (mA)"):
        """ Label the axes """
        plt.title("IT graph for sensor " + self.name)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.xlim(np.min(self.xval), np.max(self.xval))
