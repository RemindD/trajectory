#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  10:38 AM
# @Author   : Xingdong Li
# @File     : trajectory,py

import random
import numpy as np
from scipy.integrate import simps
from numpy import sin, cos, pi


class Trajectory:
    def __init__(self, constraint):
        self.constraint = constraint
        self.param = np.array([0, 0, 0, constraint[3] ** 2 / 5 + 1])

    def input_check(self):
        if len(self.constraint) != 5:
            return False
        else:
            return True

    def update(self):
        x = np.arange(0, self.param[3], float(self.param[3]) / 10)

        sf = self.param[3]
        sf2 = sf * sf
        sf3 = sf2 * sf

        px = np.array([-simps(self.sn(x, 1), x), -simps(self.sn(x, 2), x) / 2,
                       -simps(self.sn(x, 3), x) / 3, cos(self.theta(sf))])
        py = np.array([simps(self.cn(x, 1), x), simps(self.cn(x, 2), x) / 2,
                       simps(self.cn(x, 3), x) / 3, sin(self.theta(sf))])

        pt = np.array([sf, sf2 / 2, sf3 / 3, self.constraint[0] + self.param[0] * sf +
                       self.param[1] * sf2 + self.param[2] * sf3])
        pk = np.array([1, sf, sf2, self.param[0] + 2 * self.param[1] * sf +
                       3 * self.param[2] * sf2])

        pg = np.matrix([px, py, pt, pk])
        # print(pg)
        g = np.matrix([self.constraint[1] - simps(self.cn(x, 0), x),
                       self.constraint[2] - simps(self.sn(x, 0), x),
                       self.constraint[3] - self.theta(sf),
                       self.constraint[4] - (self.constraint[0] + self.param[0] * sf +
                                             self.param[1] * sf2 + self.param[2] * sf3)])
        # print(pg.I)
        print(g)
        delta = pg.I * g.T
        print(self.param)
        print(delta.T)
        # print(delta)
        # print(self.param)

        for i in range(4):
            self.param[i] += 3 * float(delta[i]) / (max(abs(delta)))

        l = simps(self.cn(x, 0), x)
        m = simps(self.sn(x, 0), x)
        print (l, m)
        return delta

    def fine_tune(self):
        if not self.input_check():
            print "Input size is not right."
            return []

        # while True:
        for i in range(1000):
            delta = self.update()
            # print ("delta", delta)
            #   norm = d_norm(delta)
            #   if norm < 10:
            #       break

        return self.param

    def theta(self, s):
        return self.constraint[0] * s + self.param[0] * s * s / 2 + \
               self.param[1] * (s ** 3) / 3 + self.param[2] * (s ** 4) / 4

    def sn(self, s, n):
        return s ** n * sin(self.theta(s))

    def cn(self, s, n):
        return s ** n * cos(self.theta(s))


def d_norm(delta):
    res = 0

    for i in range(len(delta)):
        res += delta[i] * delta[i]

    return res
