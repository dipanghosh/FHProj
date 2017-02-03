import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
plt.style.use('ggplot')
frame = pd.read_csv(sys.argv[1], header=0)
direct = os.path.dirname(sys.argv[1]) + '\\Plots'
filename = os.path.basename(sys.argv[1])
outputname, junk = os.path.splitext(direct + '\\' + filename)
df2 = frame
df2.plot(figsize=(9.6,5.4), title=filename+'hist', kind='hist', bins=100, logy = 'true')
plt.xlabel("Pubchem Activity Score")
plt.ylabel(r'Frequency')
plt.savefig(outputname + '.png')