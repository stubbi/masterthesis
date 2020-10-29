#!/usr/bin/python
import pandas as pd
import sys
import matplotlib.pyplot as plt
import statistics
from scipy.stats import kruskal

sr_restarts_learned = pd.read_csv('./SR-restarts-learned/results.csv')
sr_restarts_learned8 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 8)]['tvd'].astype(float)
sr_restarts_learned43 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 43)]['tvd'].astype(float)
sr_restarts_learned47 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 47)]['tvd'].astype(float)
sr_restarts_learned50 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 50)]['tvd'].astype(float)
sr_restarts_learned54 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 54)]['tvd'].astype(float)
sr_restarts_learned303 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#samples'] == 303)]['tvd'].astype(float)

sr_no_restarts_learned = pd.read_csv('./SR-no-restarts-learned/results.csv')
sr_no_restarts_learned8 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 8)]['tvd'].astype(float)
sr_no_restarts_learned43 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 43)]['tvd'].astype(float)
sr_no_restarts_learned47 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 47)]['tvd'].astype(float)
sr_no_restarts_learned50 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 50)]['tvd'].astype(float)
sr_no_restarts_learned54 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 54)]['tvd'].astype(float)
sr_no_restarts_learned303 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#samples'] == 303)]['tvd'].astype(float)

sr_restarts_not_learned = pd.read_csv('./SR-restarts-not-learned/results.csv')
sr_restarts_not_learned8 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 8)]['tvd'].astype(float)
sr_restarts_not_learned43 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 43)]['tvd'].astype(float)
sr_restarts_not_learned47 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 47)]['tvd'].astype(float)
sr_restarts_not_learned50 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 50)]['tvd'].astype(float)
sr_restarts_not_learned54 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 54)]['tvd'].astype(float)
sr_restarts_not_learned303 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#samples'] == 303)]['tvd'].astype(float)

am_restarts_learned = pd.read_csv('./AdaMax-restarts-learned/results.csv')
am_restarts_learned8 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 8)]['tvd'].astype(float)
am_restarts_learned43 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 43)]['tvd'].astype(float)
am_restarts_learned47 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 47)]['tvd'].astype(float)
am_restarts_learned50 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 50)]['tvd'].astype(float)
am_restarts_learned54 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 54)]['tvd'].astype(float)
am_restarts_learned303 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#samples'] == 303)]['tvd'].astype(float)

fig, axs = plt.subplots(2,2)

axs[0,0].boxplot([sr_restarts_learned8, sr_restarts_learned43, sr_restarts_learned47, sr_restarts_learned50, sr_restarts_learned54, sr_restarts_learned303])
axs[0,1].boxplot([sr_no_restarts_learned8, sr_no_restarts_learned43, sr_no_restarts_learned47, sr_no_restarts_learned50, sr_no_restarts_learned54, sr_no_restarts_learned303])
axs[1,0].boxplot([sr_restarts_not_learned8, sr_restarts_not_learned43, sr_restarts_not_learned47, sr_restarts_not_learned50, sr_restarts_not_learned54, sr_restarts_not_learned303])
axs[1,1].boxplot([am_restarts_learned8, am_restarts_learned43, am_restarts_learned47, am_restarts_learned50, am_restarts_learned54, am_restarts_learned303])

axs[0,0].set_xticklabels(['8','43','47','50','54','303'])
axs[0,1].set_xticklabels(['8','43','47','50','54','303'])
axs[1,0].set_xticklabels(['8','43','47','50','54','303'])
axs[1,1].set_xticklabels(['8','43','47','50','54','303'])

axs[0, 0].set_title('SR restarts learned')
axs[0, 1].set_title('SR no restarts learned')
axs[1, 0].set_title('SR restarts not learned')
axs[1, 1].set_title('AM restarts learned')

for ax in axs.flat:
    ax.set(xlabel='samples', ylabel='TVD')

print(f"{statistics.stdev(sr_restarts_learned8)} {statistics.mean(sr_restarts_learned8)}")
print(f"{statistics.stdev(sr_restarts_learned43)} {statistics.mean(sr_restarts_learned43)}")
print(f"{statistics.stdev(sr_restarts_learned47)} {statistics.mean(sr_restarts_learned47)}")
print(f"{statistics.stdev(sr_restarts_learned50)} {statistics.mean(sr_restarts_learned50)}")
print(f"{statistics.stdev(sr_restarts_learned54)} {statistics.mean(sr_restarts_learned54)}")
print(f"{statistics.stdev(sr_restarts_learned303)} {statistics.mean(sr_restarts_learned303)}")
print()

print(f"{statistics.stdev(sr_no_restarts_learned8)} {statistics.mean(sr_no_restarts_learned8)}")
print(f"{statistics.stdev(sr_no_restarts_learned43)} {statistics.mean(sr_no_restarts_learned43)}")
print(f"{statistics.stdev(sr_no_restarts_learned47)} {statistics.mean(sr_no_restarts_learned47)}")
print(f"{statistics.stdev(sr_no_restarts_learned50)} {statistics.mean(sr_no_restarts_learned50)}")
print(f"{statistics.stdev(sr_no_restarts_learned54)} {statistics.mean(sr_no_restarts_learned54)}")
print(f"{statistics.stdev(sr_no_restarts_learned303)} {statistics.mean(sr_no_restarts_learned303)}")
print()

print(f"{statistics.stdev(sr_restarts_not_learned8)} {statistics.mean(sr_restarts_not_learned8)}")
print(f"{statistics.stdev(sr_restarts_not_learned43)} {statistics.mean(sr_restarts_not_learned43)}")
print(f"{statistics.stdev(sr_restarts_not_learned47)} {statistics.mean(sr_restarts_not_learned47)}")
print(f"{statistics.stdev(sr_restarts_not_learned50)} {statistics.mean(sr_restarts_not_learned50)}")
print(f"{statistics.stdev(sr_restarts_not_learned54)} {statistics.mean(sr_restarts_not_learned54)}")
print(f"{statistics.stdev(sr_restarts_not_learned303)} {statistics.mean(sr_restarts_not_learned303)}")
print()

print(f"{statistics.stdev(am_restarts_learned8)} {statistics.mean(am_restarts_learned8)}")
print(f"{statistics.stdev(am_restarts_learned43)} {statistics.mean(am_restarts_learned43)}")
print(f"{statistics.stdev(am_restarts_learned47)} {statistics.mean(am_restarts_learned47)}")
print(f"{statistics.stdev(am_restarts_learned50)} {statistics.mean(am_restarts_learned50)}")
print(f"{statistics.stdev(am_restarts_learned54)} {statistics.mean(am_restarts_learned54)}")
print(f"{statistics.stdev(am_restarts_learned303)} {statistics.mean(am_restarts_learned303)}")
print()

plt.show()