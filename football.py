import pandas as pd
import seaborn 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm  


df = pd.read_table('football.txt', delim_whitespace=True)
df['outcome'] = df['favorite']- df['underdog']
df.plot.scatter(x='spread', y='outcome')
plt.show()

#ignoring games for which point spread is zero 
df.drop(df[df.spread == 0].index, inplace = True)
number_of_matches = len(df)
favorite_wins = len(df[(df['outcome']>0)])
P_favorite_wins = favorite_wins/number_of_matches
print(f"Probability of favorites winning = {P_favorite_wins}")
P_favorite_wins_x_3 =  len(df[(df['outcome']>0) & (df['spread'] ==  3.5)])/len(df[(df['spread'] == 3.5)])
print(f"Probability of favorites winning given spread is more than 3.5 = {P_favorite_wins_x_3}")
P_favorite_wins_x_y =  len(df[(df['outcome']>df['spread'])])/number_of_matches
print(f"Probability of favorites winning given outcome is more than spread = {P_favorite_wins_x_y}")

P_favorite_wins_x_m_y =  len(df[(df['outcome']>df['spread']) & (df['spread'] == 3.5) ])/len(df[(df['spread'] == 3.5)])

print(f"Probability of favorites winning given outcome is more than spread given spread is 3.5 = {P_favorite_wins_x_m_y}")
#Anomolous
P_favorite_wins_x_8 =  len(df[(df['outcome']>0) & (df['spread'] ==  8.5)])/len(df[(df['spread'] == 8.5)])
print(f"Probability of favorites winning given point spread is 8.5 = {P_favorite_wins_x_8}")
P_favorite_wins_x_9 =  len(df[(df['outcome']>0) & (df['spread'] ==  9.0)])/len(df[(df['spread'] == 9.0)])
print(f"Probability of favorites winning given point spread is 9.0 = {P_favorite_wins_x_9}")
#_________________
df['outcome - point spread'] = df['outcome'] - df['spread']
mu = df['outcome - point spread'].mean()
std = df['outcome - point spread'].std()
print(mu)
print(std)
df.hist(column='outcome - point spread',bins = 50, fill = False, density = True)
range = np.arange(-40, 40, 0.001)
plt.plot(range, norm.pdf(range,mu,std))
plt.show()

#MODEL SELECTION
mu = 0
std = 14
plt.plot(range, norm.pdf(range,mu,std))
plt.show()
print(1 - norm.cdf(x= - 3.5,loc = 0, scale = 14))
print(1 - norm.cdf(x= - 8.5,loc = 0, scale = 14))
print(1 - norm.cdf(x= - 9.0,loc = 0, scale = 14))
