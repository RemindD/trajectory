#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/4/17 9:00 PM
# @Author  : Xingdong Li
# @File    : test_case.py

import random
import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import simps


class test_case:

    case = []
    def __init__(self):
        case = []

    def generate(self):
        param = [random.uniform(-10, 10) for i in range(3)]
        param.append(5*random.random())
        a = 10 * random.random()

        self.cal(param, a)

    def calk(self, s, param, a):
        return a + param[0] * s + param[1] * (s**2) + param[2] * (s**3)

    def theta(self, s, param, a):

        if type(s) is np.ndarray:
            val = [0]
            for i in range(1, len(s)):
                sample = np.arange(0, s[i], float(i)/10)
                val.append(simps(self.calk(sample, param, a), sample))
            #print(val)
            return val
        else:
            sample = np.arange(0, s, float(s) / 10)
            return simps(self.calk(sample, param, a), sample)

    def cal(self, param, a):
        sample = np.arange(0, param[3], float(param[3])/50)

        x = simps(cos(self.theta(sample, param, a)), sample)
        y = simps(sin(self.theta(sample, param, a)), sample)
        t = self.theta(param[3], param, a)
        k = self.calk(param[3], param, a)

        self.case.append([param, [a, x, y, t, k]])
