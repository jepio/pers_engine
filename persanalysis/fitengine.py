""" Module for fitting graphs to file """
import matplotlib.pyplot as plt
from plotengine import PlotEngine
# pylint: disable=E1101
import numpy as np
from scipy.optimize import curve_fit


class FitEngine(PlotEngine):

    """ Class that performs fitting and saving of plots. """

    functions = {"lin": (lambda x, a, b: a * x + b, "A*x+B", ["A", "B"]),
                 "exp": (lambda x, a, b, c: a * np.exp(b * x) + c,
                         "A*exp(B*x)+C", ["A", "B", "C"])}

    def __init__(self, data_tuple, name, func_name):
        super(FitEngine, self).__init__(data_tuple, name)
        self.func = FitEngine.functions[func_name]
        self.fit()

    def fit(self):
        """ Fit function to data and plot. """
        popt, pcov = curve_fit(self.func[0], self.xval, self.yval)
        print "Function definition:"
        print self.func[1]
        pcov = np.sqrt(pcov)
        for i, par_val in enumerate(popt):
            string = "{0}: {1:.3g} +/- {2:.3g}".format(
                self.func[2][i], par_val, pcov[i][i])
            print string
        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()
        xvals = np.linspace(xmin, xmax, num=100)
        plt.plot(xvals, self.func[0](xvals, *popt))
        plt.ylim(ymin, ymax)
