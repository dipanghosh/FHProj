from matplotlib_venn import venn3, venn2, venn2_unweighted
from dipan_utilities import utilities
from matplotlib import pyplot as plt

activeSetf = open("/Users/dghosh/Downloads/1006_actives.csv")

activeSet = set([str.strip(i) for i in activeSetf.readlines()])
predictedSet = list(utilities.csvToSet("/Users/dghosh/Downloads/deep-vs.res"))

for i,v in enumerate(predictedSet):
    predictedSet[i] = v[:-6]

predictedSet = set(predictedSet)

print activeSet

venn2((predictedSet, activeSet), set_labels=["Predicted Set", "Active Set"])

plt.show()


