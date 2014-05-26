pers_engine
===========

### Introduction
A persistency engine to convert data from ROOT binary format to XML and subsequently analyse it. Written for my **Python in the Enterprise** class.

### Dependencies:
*   Python >=2.6
*   NumPy
*   SciPy
*   PyROOT 
*   Matplotlib

Python3 is not supported due to the fact that PyROOT doesn't work with it by default. If ROOT6 introduces support for Python3, then it will also be part of the next upgrade of pers_engine.

### Running
Run by executing either `python2.7 /path/to/persengine.py` or `/path/to/persengine.py`.

### Description
Follow the onscreen instructions. All that is required from the user is inputting digits or strings for filenames. The default functionality is to convert *input_data.root* to *input_data.xml*. This file can then be plotted and saved in *png*, *pdf*, *eps* format. The option also exists to fit a first order polynomial or an exponential function to the data.

### Future
Currently working on trending analysis.

