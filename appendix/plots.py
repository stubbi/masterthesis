#!/usr/bin/python
import pandas as pd
import sys
import matplotlib.pyplot as plt

cycles = [5,10,15,20]
iterations = [1000,10000,100000]
samples = [8, 43, 47, 50, 54, 303]

sr_restarts_learned = pd.read_csv('./SR-restarts-learned/results.csv')
sr_restarts_learned = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#cycles'].isin(cycles)) & (sr_restarts_learned['#samples'].isin(samples)) & (sr_restarts_learned['#iterations'].isin(iterations))]

sr_restarts_not_learned = pd.read_csv('./SR-restarts-not-learned/results.csv')
sr_restarts_not_learned = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#cycles'].isin(cycles)) & (sr_restarts_not_learned['#samples'].isin(samples)) & (sr_restarts_not_learned['#iterations'].isin(iterations))]

sr_no_restarts_learned = pd.read_csv('./SR-no-restarts-learned/results.csv')
sr_no_restarts_learned = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#cycles'].isin(cycles)) & (sr_no_restarts_learned['#samples'].isin(samples)) & (sr_no_restarts_learned['#iterations'].isin(iterations))]

am_restarts_learned = pd.read_csv('./AdaMax-restarts-learned/results.csv')
am_restarts_learned = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#cycles'].isin(cycles)) & (am_restarts_learned['#samples'].isin(samples)) & (am_restarts_learned['#iterations'].isin(iterations))]

x1 = sr_restarts_learned['tvd'].astype(float)
x2 = sr_restarts_not_learned['tvd'].astype(float)
x3 = sr_no_restarts_learned['tvd'].astype(float)
x4 = am_restarts_learned['tvd'].astype(float)

fig = plt.figure()
fig.suptitle(f'TVD for {cycles} cycles, {samples} samples and {iterations} iterations', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)

ax.boxplot([x1,x2,x3,x4])
plt.xticks([1,2,3,4],['SR-restarts-learned', 'SR-restarts-not-learned', 'SR-no-restarts-learned', 'AM-restarts-learned'])

ax.set_xlabel('algorithm')
ax.set_ylabel('tvd')
plt.show()
