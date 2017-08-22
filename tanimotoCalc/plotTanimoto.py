import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pickle

with open ('/Users/dghosh/Desktop/listSimAllAct', 'rb') as fp:
    listSimAllAct = pickle.load(fp)

with open ('/Users/dghosh/Desktop/listSimAllActIn', 'rb') as fp:
    listSimAllActIn = pickle.load(fp)

with open ('/Users/dghosh/Desktop/listSimAllIn', 'rb') as fp:
    listSimAllIn = pickle.load(fp)

plot = sb.kdeplot(np.array(listSimAllAct), bw=0.005, label = 'Actives and excluded')
plot = sb.kdeplot(np.array(listSimAllIn), bw=0.005, label = 'Inactives and excluded')
plot = sb.kdeplot(np.array(listSimAllActIn), bw=0.005, label = 'Actives and inactives')

plot.set(xlim=(0.2, 0.5))

plt.show()
