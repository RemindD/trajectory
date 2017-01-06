# trajectory
trajectory generation via parametric optimal control

#function of different parts
test_case.py:   generate a set of final state values using curvature function

trajectory.py:  initial a set of curvature parameters supposing a parabolic model,
                then fine-tune the initial parameters to get the trajectory

plot.py:        plot and compare the trajectories of accurate parameters and
                calculated parameters

main.py:        interface of the algorithm

#some tricky part

1. the integration among sin, cos function uses Simpson's rule

2. gradient shooting method works only in fine-tune period

3. Initial the parameters via:

    b = (k_f^2 - k_0^2) / (2*theta_f)
    
    s = 2 * theta_f / (k_0 + k_f)
    
    c = d = 0
 
