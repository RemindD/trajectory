#!/usr/bin/env python
# -*- coding: utf8 -*-
# @Time     :  1:49 PM
# @Author   : Xingdong Li
# @File     : main,py

from trajectory import *
from test_case import *
from plot import *


def main():

    case = test_case()

    case.generate()

    print(case.case[0])
    '''
    new_traj = Trajectory(
        [3.2832521833924955, -0.0057374001018736191, 0.61065648092059921, 3.380510083314959, 4.361349932557083],
        [-0.043305826859034724, -1.9372809678470935, 3.0586845438707155, 1.0])
    '''
    new_traj = Trajectory(case.case[0][1], case.case[0][0])
    param = new_traj.fine_tune()

    print fplot(case.case[0][1][0], case.case[0][0], param)

    print(case.case[0][0], param)

main()
