""" Module for plotting a trend in data to a file """
# pylint: disable=E1101
from fitengine import FitEngine
import numpy as np


class TrendEngine(FitEngine):

    """ Class that performs trend analysis of data, then fits and plots it. """

    def __init__(self, ioh_obj, point_num=None, xcoord=None):
        self.xval = []
        self.yval = []
        self.yerr = []
        self.xerr = None
        if point_num is not None:
            data_tuple = self.select(ioh_obj, point_num)
        elif xcoord is not None:
            data_tuple = self.selectx(ioh_obj, xcoord)
        name = "point" + str(point_num)
        if len(data_tuple[0]) < 2:
            print "Can't fit curve, not enough points"
            super(FitEngine, self).__init__(data_tuple, name)
        else:
            super(TrendEngine, self).__init__(data_tuple, name, "lin")
        self.style(xlabel="Time (weeks)", title="Trend for ")
        self.xlimits(-1, 86)
        if len(self.xval) > 0:
            self.ylimits(0, np.max(self.yval) * 1.2)

    def select(self, ioh_obj, point_num):
        """
        Select points with number point_num from all graphs and return them.
        """
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
