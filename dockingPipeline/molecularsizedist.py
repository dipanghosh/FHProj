from rdkit import Chem
from rdkit.Chem import Descriptors
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

moleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/2624743101925829136.sdf")
molwtlist = []
for i,m in enumerate(moleculeSet):
    print i
    molwtlist.append(Descriptors.MolWt(m))

sb.kdeplot(np.array(molwtlist), bw=10, label = 'Molecular weight')
print np.mean(np.array(molwtlist))
print np.var(np.array(molwtlist))
print np.std(np.array(molwtlist))
plt.show()