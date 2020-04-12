import random 
import numpy as np
import matplotlib.pyplot as plt

def Mean(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    mean = sum_num / len(num)
    return mean

def Sigma(num):
    M = Mean(num)
    sum_num = 0
    for t in num:
        sum_num = sum_num + (t - M)**2           

    Sigma = sum_num / len(num)

    return Sigma

N  = 1000
Y = []
mu_m = 175
mu_f = 160
sigma = 2

for i in range(N):
    G = random.randint(0, 1)
    if G == 0:
        s = int(np.random.normal(mu_m, sigma, 1)[0])
        Y.append(s)
    else: 
        s = int(np.random.normal(mu_f, sigma, 1)[0])
        Y.append(s)
M = Mean(Y)
S = Sigma(Y)
print(f"Mean of the heights is {M}")
print(f"Variance of the heights is {S}")
plt.hist(Y, density=True, bins=60)
plt.show()
