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
        param = [random.uniform(-10.0 / (i + 1), 10.0 / (i + 1)) for i in range(3)]
        param.append(random.random())
        param = [-0.043305826859034724, -1.9372809678470935, 3.0586845438707155, 1.0]
        a = 10 * random.random()
        a = 3.2832521833924955

        self.cal(param, a)

    def calk(self, s, param, a):
        return a + param[0] * s + param[1] * (s**2) + param[2] * (s**3)

    def theta(self, s, param, a):
        return a * s + param[0] * (s ** 2) / 2 + param[1] * (s ** 3) / 3 + \
               param[2] * (s ** 4) / 4

    def cal(self, param, a):
        sample = np.arange(0, param[3], float(param[3])/50)

        x = simps(cos(self.theta(sample, param, a)), sample)
        y = simps(sin(self.theta(sample, param, a)), sample)
        t = self.theta(param[3], param, a)
        k = self.calk(param[3], param, a)

        self.case.append([param, [a, x, y, t, k]])
