import model as mo
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iterate = 500
min = 1
max = 30

suppler, demander = mo.initiate(min, max)

adam = (max + min) / 2

ava = pd.Series(adam-suppler)

ava2 = pd.Series(demander-adam)

trade2 = len(ava2[ava2 > 0])

trade = len(ava[ava > 0])

adamAu = ava[ava > 0].sum() + ava2[ava2 > 0].sum()

def report(baza, bazaVol):

    print(

        '''
        iterates: %d
        suppler: %d
        demander: %d
        baza trade mean: %f
        baza trade std: %f
        baza trade volume: %f
        '''%(iterate, len(suppler), len(demander),np.mean(baza), np.std(baza), np.sum(np.array(bazaVol)))

    )

sns.set()

baza, bazaVol, au = mo.tradeIterate(initSuppler=suppler, initDemander=demander, iterNum=iterate)

sns.histplot(suppler,alpha=0.7, label="supply", color="orange", bins=30)
sns.histplot(demander,alpha=0.7, label="demand",bins=30)
plt.legend()
plt.axvline(adam, color="green")
plt.show()


fig, ax = plt.subplots(nrows=2, figsize=(10, 7))
ax1 = ax[0]
sns.histplot(baza, bins=20, ax=ax1, label="baza trade price")
ax1.axvline(adam, color="orange", label="Competitive Equilibrium")
ax1.axvline(np.mean(baza), color="blue", linestyle="-.")
ax1.legend()
ax2 = ax[1]
ax2.plot(pd.Series(bazaVol).cumsum(), label="baza cumulative trade volume")
ax2.axhline(trade, color="green", label="Competitive Equilibrium")
ax2.legend()
plt.show()

if trade == trade2:

    print("Adam Smith Optimize True.")


baza1 = baza
bazaVol1 = bazaVol




experimentIterate = 100

auList = []

for n in range(experimentIterate):

    baza, bazaVol, au = mo.tradeIterate(initSuppler=suppler, initDemander=demander, iterNum=iterate)

    auList.append(au)

sns.histplot(auList, bins=10)
plt.axvline(adamAu)
plt.show()

report(baza1, bazaVol1)