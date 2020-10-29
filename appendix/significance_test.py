#!/usr/bin/python
import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy.stats import kruskal
import statistics

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

print(f"{statistics.stdev(x1)} {statistics.mean(x1)}")
print(f"{statistics.stdev(x2)} {statistics.mean(x2)}")
print(f"{statistics.stdev(x3)} {statistics.mean(x3)}")
print(f"{statistics.stdev(x4)} {statistics.mean(x4)}")

stat, p = kruskal(x1, x2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')

