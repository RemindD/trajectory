#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  10:38 AM
# @Author   : Xingdong Li
# @File     : trajectory.py

import random
import numpy as np
from scipy.integrate import simps
import math
from numpy import sin, cos, pi
from plot import *


class Trajectory:
    def __init__(self, constraint):
        self.constraint = constraint
        '''
        self.param = np.array([0.5 * (constraint[4] ** 2 - constraint[0] ** 2) / constraint[3],
                               0, 0,
                               2 * abs((constraint[3] / (constraint[0] + constraint[4])))])
        '''
        d = math.sqrt(float(constraint[1] ** 2 + constraint[2] ** 2))
        s = d * (constraint[3] ** 2 / 5 + 1) + 2 * abs(constraint[3]) / 5
        b = 6 * constraint[3] / (s ** 2) - 2 * constraint[0] / s + 4 * constraint[4] / s
        c = 3 * (constraint[0] + constraint[4]) / (s ** 2) + 6 * constraint[3] / (s ** 3)
        self.param = np.array([b, c, 0, s])

    def input_check(self):
        if len(self.constraint) != 5:
            return False
        else:
            return True

    def update(self, scale):
        x = np.arange(0, self.param[3], float(self.param[3]) / 100)
        cosx = cos(self.theta(x))
        sinx = sin(self.theta(x))
        x2 = np.power(x, 2)
        x3 = np.power(x, 3)
        x4 = np.power(x, 4)
        sf = self.param[3]
        sf2 = sf * sf
        sf3 = sf2 * sf
        sf4 = sf2 * sf2
        '''
        px = np.array([-simps(self.sn(x, 2), x) / 2, -simps(self.sn(x, 3), x) / 3,
                       -simps(self.sn(x, 4), x) / 4, cos(self.theta(sf))])
        py = np.array([simps(self.cn(x, 2), x) / 2, simps(self.cn(x, 3), x) / 3,
                       simps(self.cn(x, 4), x) / 4, sin(self.theta(sf))])
        '''

        px = np.array([-simps(np.multiply(sinx, x2), x) / 2, -simps(np.multiply(sinx, x3), x) / 3,
                       -simps(np.multiply(sinx, x4), x) / 4, cosx[len(cosx)-1]])
        py = np.array([simps(np.multiply(cosx, x2), x) / 2, simps(np.multiply(cosx, x3), x) / 3,
                       simps(np.multiply(cosx, x4), x) / 4, sinx[len(sinx)-1]])

        pt = np.array([sf2 / 2, sf3 / 3, sf4 / 4, self.calk(sf)])
        pk = np.array([sf, sf2, sf3, self.param[0] + 2 * self.param[1] * sf +
                       3 * self.param[2] * sf2])

        pg = np.matrix([px, py, pt, pk])
        '''
        g = np.matrix([self.constraint[1] - simps(self.cn(x, 0), x),
                       self.constraint[2] - simps(self.sn(x, 0), x),
                       self.constraint[3] - self.theta(sf),
                       self.constraint[4] - self.calk(sf)
                       ])
        '''
        g = np.matrix([self.constraint[1] - simps(cosx, x),
                       self.constraint[2] - simps(sinx, x),
                       self.constraint[3] - self.theta(sf),
                       self.constraint[4] - self.calk(sf)
                       ])
        delta = np.linalg.inv(pg) * g.transpose()

        for i in range(4):
            self.param[i] += delta[i] * scale

    def fine_tune(self):
        if not self.input_check():
            print "Input size is not right."
            return []

        self.update(0.2)
        self.update(0.2)
        self.update(0.2)
        self.update(0.2)
        self.update(0.3)
        self.update(0.5)
        self.update(0.6)
        self.update(0.8)
        self.update(1.0)

        return self.param

    def theta(self, s):
        res = self.param[2] / 4.0 * s
        res = np.multiply(res + self.param[1] / 3.0, s)
        res = np.multiply(res + self.param[0] / 2.0, s)
        res = np.multiply(res + self.constraint[0], s)
        return res

    def calk(self, s):
        res = self.param[2] * s
        res = np.multiply(res + self.param[1], s)
        res = np.multiply(res + self.param[0], s)
        res = res + self.constraint[0]

        return res

    def sn(self, s, n):
        return (s ** n) * sin(self.theta(s))

    def cn(self, s, n):
        return (s ** n) * cos(self.theta(s))


