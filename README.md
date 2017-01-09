# trajectory
trajectory generation via parametric optimal control

#function of different parts
test_case.py:   generate a set of final state values using curvature function

trajectory.py:  initial a set of curvature parameters supposing a parabolic model,
                then fine-tune the initial parameters to get the trajectory

plot.py:        plot and compare the trajectories of accurate parameters and
                calculated parameters or just plot an single calculated trajectory

main.py:        interface of the algorithm

#some tricky part

1. the integration among sin, cos function uses Simpson's rule

2. gradient shooting method works only in fine-tune period

3. Initial the parameters via:

    s = s = d * (theta_f ** 2 / 5 + 1) + 2 * abs(theta_f) / 5
    
    b = 6 * theta_f / (s ** 2) - 2 * k_0 / s + 4 * k_f / s
    
    c = 3 * (k_0 + k_f) / (s ** 2) + 6 * theta_f / (s ** 3)

    d = 0
    
4. changes of parameters need to be scaled down to preserve the stability

    current scalability factor is (# of iteration) / 5
    
5. due to the effect of scalability, the number of epics need to increase from 3 to 5

    which leads to less efficiency.
 
