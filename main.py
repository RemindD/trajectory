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

    case = test_case()

    case.generate()
    print len(case.case)

    # time1 = time.time()
    # for i in range(len(case.case)):
    #    new_traj = Trajectory(case.case[i][1])
    #    param = new_traj.fine_tune()

    # time2 = time.time()

    # print (time2 - time1) / len(case.case)

    new_case = [0, 0, 5, pi / 2, 0]
    new_traj = Trajectory(new_case)
    param = new_traj.fine_tune()
    print param
    plot(0, param)
main()
