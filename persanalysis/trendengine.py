""" Module for plotting a trend in data to a file """
# pylint: disable=E1101
from fitengine import FitEngine
import numpy as np


class TrendEngine(FitEngine):

    """ Class that performs trend analysis of data, then fits and plots it. """

    def __init__(self, ioh_obj, point_num):
        self.xval = []
        self.yval = []
        self.yerr = []
        self.xerr = None
        data_tuple = self.select(ioh_obj, point_num)
        name = "trend_point" + str(point_num)
        super(TrendEngine, self).__init__(data_tuple, name, "lin")
        self.style(xlabel="Time (weeks)")

    def select(self, ioh_obj, point_num):
        """ Select point number point_num from all graphs and return them. """
        for i, graph_name in enumerate(ioh_obj.xmlindex()):
            xval, yval, _, yerr = ioh_obj.memgrabgraph(graph_name)
            if point_num in xrange(len(xval)):
                self.xval.append(i)
                self.yval.append(yval[point_num])
                self.yerr.append(yerr[point_num])
        self.xval = np.array(self.xval)
        self.yval = np.array(self.yval)
        self.yerr = np.array(self.yerr)
        return self.xval, self.yval, self.xerr, self.yerr
