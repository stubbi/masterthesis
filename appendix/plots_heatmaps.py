#!/usr/bin/python
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy.stats import kruskal


cycles = [5, 10, 15, 20]
iterations = [1000,10000,100000]
samples = [8, 43, 47, 50, 54, 303]
algorithms = {'SR-restarts-learned': 'Stochastic Reconfiguration Restarts Learned',
                'SR-no-restarts-learned': 'Stochastic Reconfiguration without Restarts Learned',
                'SR-restarts-not-learned': 'Stochastic Reconfiguration Restarts Exact',
                'AdaMax-restarts-learned': 'AdaMax Restarts Learned'}

for v in ['Min', 'Mean']:
    for a in algorithms:
        fig, axs = plt.subplots(2,2)
        raw = pd.read_csv(f'./{a}/results.csv')
        for c in cycles:
            data = []
            for i in iterations:
                row = []
                for s in samples:
                    filtered = raw[(raw['success']==True) & (raw['#cycles'] == c) & (raw['#samples'] == s) & (raw['#iterations'] == i)]['tvd'].astype(float)
                    e = 0
                    if len(filtered) > 0:
                        if v == 'Min':
                            e = min(filtered)
                        elif v == 'Mean':
                            e = statistics.mean(filtered)
                    row.append(e)
                data.append(row)
            
            if c == 5:
                idx1 = 0
                idx2 = 0
            elif c == 10:
                idx1 = 0
                idx2 = 1
            elif c == 15:
                idx1 = 1
                idx2 = 0
            elif c ==20:
                idx1 = 1
                idx2 = 1

            ax = axs[idx1, idx2]
            im = ax.imshow(data, vmin=0, vmax=1)

            # We want to show all ticks...
            ax.set_xticks(np.arange(len(samples)))
            ax.set_yticks(np.arange(len(iterations)))
            # ... and label them with the respective list entries
            ax.set_xticklabels(samples)
            ax.set_yticklabels(iterations)

            # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                    rotation_mode="anchor")

            # Loop over data dimensions and create text annotations.
            for i in range(len(iterations)):
                for j in range(len(samples)):
                    t = 'n/a'
                    if data[i][j] != 0:
                        t = format(data[i][j], '.2f')
                    text = ax.text(j, i, t, ha="center", va="center", color="w")
            
            ax.set_title(f'{c} Cycles')
            for ax in axs.flat:
                ax.set(xlabel='Samples', ylabel='Iterations')

            fig.tight_layout()

        plt.savefig(f'tvd_heatmap_{algorithms[a]}.pdf')
        plt.close()