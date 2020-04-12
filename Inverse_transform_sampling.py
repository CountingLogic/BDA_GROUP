import math
import random 
import numpy as np
import matplotlib.pyplot as plt

def Exponential(N,l):
    return np.random.exponential(1/l, N)


def CDF_Inv(N,l):
    U = random.sample(range(2,10000), N)
    print(U)

    Dis = [math.log(1-u)**2 for u in U]
    return Dis 





Dist = Exponential(1000,0.5)
Dis = CDF_Inv(1000,0.5)
plt.hist(Dist, density=True, bins=30)
plt.hist(Dis, density=True, bins=30)
plt.show()

    

