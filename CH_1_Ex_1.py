import numpy as np
import matplotlib.pyplot as plt


r = 0.1

def time(r):
    time = []
    for i in range(100):
        sum_ = 0
        time_ = 0
        while sum_ < r:
            sum_ = sum_ + np.random.randn(1)[0]
            time_ = time_ + 1
        time.append(time_)
    return sum(time)

data = [time(r) for i in range(10)]
print(data)

hx, hy, _ = plt.hist(data, bins=50, normed=1,color="lightblue")

plt.ylim(0.0,max(hx)+0.000005)
plt.title('Generate random numbers \n from a standard normal distribution with python')
plt.grid()

plt.savefig("numpy_random_numbers_stantard_normal_distribution.png", bbox_inches='tight')
plt.show()
