#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  3:22 PM
# @Author   : Xingdong Li
# @File     : plot,py

import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt


def fplot(a, param1, param2):
    x1, y1 = caltraj(a, param1)
    x2, y2 = caltraj(a, param2)
    plt.subplot(121)
    plt.plot(x1, y1)
    plt.subplot(122)
    plt.plot(x2, y2)
    plt.show()


def caltraj(a, param):
    sample = np.arange(0, param[3], param[3] / 1000)
    x = [0]
    y = [0]

    for i in range(1, len(sample)):
        subs = np.arange(0, sample[i], sample[i] / 1000)
        x.append(simps(np.cos(theta(subs, a, param)), subs))
        y.append(simps(np.sin(theta(subs, a, param)), subs))
    return x, y


def theta(s, a, param):
    return a * s + param[0] * s * s / 2 + \
           param[1] * (s ** 3) / 3 + param[2] * (s ** 4) / 4
