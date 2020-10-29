#!/usr/bin/python
import pandas as pd
import sys
import matplotlib.pyplot as plt
import statistics
from scipy.stats import kruskal

sr_restarts_learned = pd.read_csv('./SR-restarts-learned/results.csv')
sr_restarts_learned1000 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#iterations'] == 1000)]['tvd'].astype(float)
sr_restarts_learned10000 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#iterations'] == 10000)]['tvd'].astype(float)
sr_restarts_learned100000 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#iterations'] == 100000)]['tvd'].astype(float)

sr_no_restarts_learned = pd.read_csv('./SR-no-restarts-learned/results.csv')
sr_no_restarts_learned1000 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#iterations'] == 1000)]['tvd'].astype(float)
sr_no_restarts_learned10000 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#iterations'] == 10000)]['tvd'].astype(float)
sr_no_restarts_learned100000 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#iterations'] == 100000)]['tvd'].astype(float)

sr_restarts_not_learned = pd.read_csv('./SR-restarts-not-learned/results.csv')
sr_restarts_not_learned1000 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#iterations'] == 1000)]['tvd'].astype(float)
sr_restarts_not_learned10000 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#iterations'] == 10000)]['tvd'].astype(float)
sr_restarts_not_learned100000 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#iterations'] == 100000)]['tvd'].astype(float)

am_restarts_learned = pd.read_csv('./AdaMax-restarts-learned/results.csv')
am_restarts_learned1000 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#iterations'] == 1000)]['tvd'].astype(float)
am_restarts_learned10000 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#iterations'] == 10000)]['tvd'].astype(float)
am_restarts_learned100000 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#iterations'] == 100000)]['tvd'].astype(float)

fig, axs = plt.subplots(2,2)

axs[0,0].boxplot([sr_restarts_learned1000, sr_restarts_learned10000, sr_restarts_learned100000])
axs[0,1].boxplot([sr_no_restarts_learned1000, sr_no_restarts_learned10000, sr_no_restarts_learned100000])
axs[1,0].boxplot([sr_restarts_not_learned1000, sr_restarts_not_learned10000, sr_restarts_not_learned100000])
axs[1,1].boxplot([am_restarts_learned1000, am_restarts_learned10000, am_restarts_learned100000])

axs[0,0].set_xticklabels(['1.000', '10.000', '100.000'])
axs[0,1].set_xticklabels(['1.000', '10.000', '100.000'])
axs[1,0].set_xticklabels(['1.000', '10.000', '100.000'])
axs[1,1].set_xticklabels(['1.000', '10.000', '100.000'])

axs[0, 0].set_title('SR restarts learned')
axs[0, 1].set_title('SR no restarts learned')
axs[1, 0].set_title('SR restarts not learned')
axs[1, 1].set_title('AM restarts learned')

for ax in axs.flat:
    ax.set(xlabel='iterations', ylabel='TVD')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

print(f"{statistics.stdev(sr_restarts_learned1000)} {statistics.mean(sr_restarts_learned1000)}")
print(f"{statistics.stdev(sr_restarts_learned10000)} {statistics.mean(sr_restarts_learned10000)}")
print(f"{statistics.stdev(sr_restarts_learned100000)} {statistics.mean(sr_restarts_learned100000)}")
print()
	
print(f"{statistics.stdev(sr_no_restarts_learned1000)} {statistics.mean(sr_no_restarts_learned1000)}")
print(f"{statistics.stdev(sr_no_restarts_learned10000)} {statistics.mean(sr_no_restarts_learned10000)}")
print(f"{statistics.stdev(sr_no_restarts_learned100000)} {statistics.mean(sr_no_restarts_learned100000)}")
print()

print(f"{statistics.stdev(sr_restarts_not_learned1000)} {statistics.mean(sr_restarts_not_learned1000)}")
print(f"{statistics.stdev(sr_restarts_not_learned10000)} {statistics.mean(sr_restarts_not_learned10000)}")
print(f"{statistics.stdev(sr_restarts_not_learned100000)} {statistics.mean(sr_restarts_not_learned100000)}")
print()

print(f"{statistics.stdev(am_restarts_learned1000)} {statistics.mean(am_restarts_learned1000)}")
print(f"{statistics.stdev(am_restarts_learned10000)} {statistics.mean(am_restarts_learned10000)}")
print(f"{statistics.stdev(am_restarts_learned100000)} {statistics.mean(am_restarts_learned100000)}")
plt.show()