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
    # case.generate()
    # print len(case.case)

    # time1 = time.time()
    # for i in range(len(case.case)):
    #    new_traj = Trajectory(case.case[i][1])
    #    param = new_traj.fine_tune()

    # time2 = time.time()

    # print (time2 - time1) / len(case.case)
    time1 = time.time()
    false = 0
    for i in range(200):
        a = random.uniform(-0.1, 0.1)
        new_case = [a, random.uniform(5, 15), random.uniform(-5, 5),
                    random.uniform(-1 * pi / 2, 1 * pi / 2), random.uniform(-0.1, 0.1)]
        new_traj = Trajectory(new_case)
        param = new_traj.fine_tune()
        #plot(a, param)

        x = np.arange(0, new_traj.param[3], float(new_traj.param[3]) / 1000)
        g = [new_traj.constraint[1] - simps(new_traj.cn(x, 0), x),
             new_traj.constraint[2] - simps(new_traj.sn(x, 0), x),
             new_traj.constraint[3] - new_traj.theta(new_traj.param[3]),
             new_traj.constraint[4] - new_traj.calk(new_traj.param[3])]
        #print g
        if abs(g[0])+abs(g[1])+abs(g[2])+abs(g[3])>1:
            false += 1

        #print param
    time2 = time.time()
    print (time2 - time1) / 200.0
    print false / 200.0
main()
