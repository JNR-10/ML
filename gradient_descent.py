import numpy as np
import math

def gradient_descent(x,y):
        m_curr = b_curr = 0 #starting with 0 and then taking the steps to reach global minima
        iterations = 10000 #number of steps required to reach
        n = len(x)
        learning_rate = 0.002 #using trial and error
        exponent = -20

        cost_previous = 0

        for i in range(iterations):
            y_predicted = m_curr * x + b_curr
            cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
            md = -(2/n)*sum(x*(y-y_predicted))
            bd = -(2/n)*sum(y-y_predicted)
            m_curr = m_curr - learning_rate * md
            b_curr = b_curr - learning_rate * bd
            if math.isclose(cost,cost_previous,rel_tol=math.exp(exponent),abs_tol=0.0):
                    break
            cost_previous = cost
            print("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost,i))
    

x = np.array([92,56,88,70,80,49,65,35,66,67])
y = np.array([98,68,81,80,83,52,66,30,68,73])

gradient_descent(x,y)
