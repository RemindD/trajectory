#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  1:49 PM
# @Author   : Xingdong Li
# @File     : main,py

from trajectory import *
from test_case import *


def main():
    testcase = [0, 5, 0, 3 * pi / 4, 0]

    case = test_case()

    case.generate()

    print(case.case[0])

    new_traj = Trajectory(case.case[0][1])

    param = new_traj.fine_tune()

    print(param)


main()
