#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', family='serif')
matplotlib.rc('font', serif='Computer Modern Roman')
matplotlib.rc('text', usetex=True)
matplotlib.rc('ps', usedistiller='xpdf')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')

plt.savefig('testPlot.png', bbox_inches='tight')
plt.show()
