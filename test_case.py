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
        for i in range(1000):
            param = [random.uniform(-10.0, 10.0) for i in range(3)]
            param.append(random.random())
            a = random.uniform(-5.0, 5.0)

            self.cal(param, a)

    def calk(self, s, param, a):
        return a + param[0] * s + param[1] * (s**2) + param[2] * (s**3)

    def theta(self, s, param, a):
        return a * s + param[0] * (s ** 2) / 2 + param[1] * (s ** 3) / 3 + \
               param[2] * (s ** 4) / 4

    def cal(self, param, a):
        sample = np.arange(0, param[3], float(param[3])/1000)

        x = simps(cos(self.theta(sample, param, a)), sample)
        y = simps(sin(self.theta(sample, param, a)), sample)
        sample_t = self.theta(sample, param, a)
        for i in range(len(sample_t)):
            if abs(sample_t[i] > pi / 2):
                return
        t = self.theta(param[3], param, a)
        k = self.calk(param[3], param, a)

        if abs(t) < pi / 2:
            self.case.append([param, [a, x, y, t, k]])
