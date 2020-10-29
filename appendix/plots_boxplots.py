#!/usr/bin/python
import pandas as pd
import sys
import matplotlib.pyplot as plt
import statistics
from scipy.stats import kruskal

sr_restarts_learned = pd.read_csv('./SR-restarts-learned/results.csv')
sr_restarts_learned5 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#cycles'] == 5)]
sr_restarts_learned10 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#cycles'] == 10)]
sr_restarts_learned15 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#cycles'] == 15)]
sr_restarts_learned20 = sr_restarts_learned[(sr_restarts_learned['success']==True) & (sr_restarts_learned['#cycles'] == 20)]
sr_restarts_learnedall = sr_restarts_learned[(sr_restarts_learned['success']==True)]

sr_no_restarts_learned = pd.read_csv('./SR-no-restarts-learned/results.csv')
sr_no_restarts_learned5 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#cycles'] == 5)]
sr_no_restarts_learned10 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#cycles'] == 10)]
sr_no_restarts_learned15 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#cycles'] == 15)]
sr_no_restarts_learned20 = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True) & (sr_no_restarts_learned['#cycles'] == 20)]
sr_no_restarts_learnedall = sr_no_restarts_learned[(sr_no_restarts_learned['success']==True)]

sr_restarts_not_learned = pd.read_csv('./SR-restarts-not-learned/results.csv')
sr_restarts_not_learned5 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#cycles'] == 5)]
sr_restarts_not_learned10 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#cycles'] == 10)]
sr_restarts_not_learned15 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#cycles'] == 15)]
sr_restarts_not_learned20 = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True) & (sr_restarts_not_learned['#cycles'] == 20)]
sr_restarts_not_learnedall = sr_restarts_not_learned[(sr_restarts_not_learned['success']==True)]

am_restarts_learned = pd.read_csv('./AdaMax-restarts-learned/results.csv')
am_restarts_learned5 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#cycles'] == 5)]
am_restarts_learned10 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#cycles'] == 10)]
am_restarts_learned15 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#cycles'] == 15)]
am_restarts_learned20 = am_restarts_learned[(am_restarts_learned['success']==True) & (am_restarts_learned['#cycles'] == 20)]
am_restarts_learnedall = am_restarts_learned[(am_restarts_learned['success']==True)]

sr5 = sr_restarts_learned5['tvd'].astype(float)
sr5not = sr_restarts_not_learned5['tvd'].astype(float)
sr5no = sr_no_restarts_learned5['tvd'].astype(float)
am5 = am_restarts_learned5['tvd'].astype(float)

sr10 = sr_restarts_learned10['tvd'].astype(float)
sr10not = sr_restarts_not_learned10['tvd'].astype(float)
sr10no = sr_no_restarts_learned10['tvd'].astype(float)
am10 = am_restarts_learned10['tvd'].astype(float)

sr15 = sr_restarts_learned15['tvd'].astype(float)
sr15not = sr_restarts_not_learned15['tvd'].astype(float)
sr15no = sr_no_restarts_learned15['tvd'].astype(float)
am15 = am_restarts_learned15['tvd'].astype(float)

sr20 = sr_restarts_learned20['tvd'].astype(float)
sr20not = sr_restarts_not_learned20['tvd'].astype(float)
sr20no = sr_no_restarts_learned20['tvd'].astype(float)
am20 = am_restarts_learned20['tvd'].astype(float)

srall = sr_restarts_learnedall['tvd'].astype(float)
srallnot = sr_restarts_not_learnedall['tvd'].astype(float)
srallno = sr_no_restarts_learnedall['tvd'].astype(float)
amall = am_restarts_learnedall['tvd'].astype(float)


fig, axs = plt.subplots(2,2)

axs[0,0].boxplot([sr5, sr5no, sr5not, am5])
axs[0,1].boxplot([sr10, sr10no, sr10not, am10])
axs[1,0].boxplot([sr15, sr15no, sr15not, am15])
axs[1,1].boxplot([sr20, sr20no, sr20not, am20])

axs[0,0].set_xticklabels(['SR Restarts Learned', 'SR no Restarts Learned', 'SR Restarts Exact', 'AdaMax Restarts Learned'])
axs[0,1].set_xticklabels(['SR Restarts Learned', 'SR no Restarts Learned', 'SR Restarts Exact', 'AdaMax Restarts Learned'])
axs[1,0].set_xticklabels(['SR Restarts Learned', 'SR no Restarts Learned', 'SR Restarts Exact', 'AdaMax Restarts Learned'])
axs[1,1].set_xticklabels(['SR Restarts Learned', 'SR no Restarts Learned', 'SR Restarts Exact', 'AdaMax Restarts Learned'])

axs[0, 0].set_title('5 Cycles')
axs[0, 1].set_title('10 Cycles')
axs[1, 0].set_title('15 Cycles')
axs[1, 1].set_title('20 Cycles')

for ax in axs.flat:
    ax.set(ylabel='TVD')

print(f"{statistics.stdev(sr5)} {statistics.mean(sr5)}")
print(f"{statistics.stdev(sr10)} {statistics.mean(sr10)}")
print(f"{statistics.stdev(sr15)} {statistics.mean(sr15)}")
print(f"{statistics.stdev(sr20)} {statistics.mean(sr20)}")

print()

print(f"{statistics.stdev(sr5no)} {statistics.mean(sr5no)}")
print(f"{statistics.stdev(sr10no)} {statistics.mean(sr10no)}")
print(f"{statistics.stdev(sr15no)} {statistics.mean(sr15no)}")
print(f"{statistics.stdev(sr20no)} {statistics.mean(sr20no)}")

stat, p = kruskal(srall, srallno)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')

plt.show()