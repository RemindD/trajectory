#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  1:49 PM
# @Author   : Xingdong Li
# @File     : main,py

from trajectory import *
from test_case import *
from plot import *
import time


def main():
    # case = test_case()
    print pi
    # case.generate()
    # print len(case.case)

    # time1 = time.time()
    # for i in range(len(case.case)):
    #    new_traj = Trajectory(case.case[i][1])
    #    param = new_traj.fine_tune()

    # time2 = time.time()

    # print (time2 - time1) / len(case.case)
    for i in range(10):
        new_case = [random.uniform(-0.1, 0.1), random.uniform(5, 15), random.uniform(-5, 5),
                    random.uniform(-4 * pi / 5, 4 * pi / 5), random.uniform(-0.1, 0.1)]
        new_traj = Trajectory(new_case)
        param = new_traj.fine_tune()
        print param
        plot(0, param)
main()
