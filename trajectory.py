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
    def __init__(self, constraint, realparam):
        self.constraint = constraint
        print realparam
        self.param = np.array([random.random(), random.random(),
                               random.random(), 0.9])
        # self.param = np.array(realparam)
        print(self.param)

    def input_check(self):
        if len(self.constraint) != 5:
            return False
        else:
            return True

    def update(self):
        x = np.arange(0, self.param[3], float(self.param[3]) / 10000)

        sf = self.param[3]
        sf2 = sf * sf
        sf3 = sf2 * sf
        sf4 = sf2 * sf2

        px = np.array([-simps(self.sn(x, 2), x) / 2, -simps(self.sn(x, 3), x) / 3,
                       -simps(self.sn(x, 4), x) / 4, cos(self.theta(sf))])
        py = np.array([simps(self.cn(x, 2), x) / 2, simps(self.cn(x, 3), x) / 3,
                       simps(self.cn(x, 4), x) / 4, sin(self.theta(sf))])

        pt = np.array([sf2 / 2, sf3 / 3, sf4 / 4, self.calk(sf)])
        pk = np.array([sf, sf2, sf3, self.param[0] + 2 * self.param[1] * sf +
                       3 * self.param[2] * sf2])

        pg = np.matrix([px, py, pt, pk])

        g = np.matrix([self.constraint[1] - simps(self.cn(x, 0), x),
                       self.constraint[2] - simps(self.sn(x, 0), x),
                       self.constraint[3] - self.theta(sf),
                       self.constraint[4] - self.calk(sf)
                       ])
        print ("g", g)
        delta = np.linalg.pinv(pg) * g.transpose()
        # print("param", self.param)

        print("delta", delta.T)


        for i in range(4):
            self.param[i] += delta[i]

        return delta

    def fine_tune(self):
        if not self.input_check():
            print "Input size is not right."
            return []

        for i in range(10):
            delta = self.update()

        return self.param

    def theta(self, s):
        return self.constraint[0] * s + self.param[0] * s * s / 2 + \
               self.param[1] * (s ** 3) / 3 + self.param[2] * (s ** 4) / 4

    def calk(self, s):
        return self.constraint[0] + self.param[0] * s + \
               self.param[1] * (s ** 2) + self.param[2] * (s ** 3)

    def sn(self, s, n):
        return (s ** n) * sin(self.theta(s))

    def cn(self, s, n):
        return (s ** n) * cos(self.theta(s))


def d_norm(delta):
    res = 0

    for i in range(len(delta)):
        res += delta[i] * delta[i]

    return res
