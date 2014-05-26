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
        return name

    def style(self, xlabel=r'Temperature ($^\circ$C)',
              ylabel="Current (mA)", title="IT graph for sensor "):
        """ Label the axes """

        plt.title(title + self.name)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.xlim(np.min(self.xval), np.max(self.xval))

    @staticmethod
    def close():
        """ Close the current plot in case of failed input. """
        plt.close()

    @staticmethod
    def ylimits(ymin, ymax):
        """ Change plot y axis limits. """
        plt.ylim(ymin, ymax)

    @staticmethod
    def xlimits(xmin, xmax):
        """ Change plot x axis limits. """
        plt.xlim(xmin, xmax)
