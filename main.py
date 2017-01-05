#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  1:49 PM
# @Author   : Xingdong Li
# @File     : main,py

from trajectory import *


def main():
    test_case = [0, 5, 0, 3 * pi / 4, 0]

    new_traj = Trajectory(test_case)

    param = new_traj.fine_tune()

    print(param)


main()
