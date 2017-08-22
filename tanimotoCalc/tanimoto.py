from rdkit import Chem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from multiprocessing import Pool
from dipan_utilities import pyDec, utilities

activeMoleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/combinedactive.sdf")
inactiveMoleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/randlist.sdf")
excludedMoleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/excluded.sdf")

fingerprintSetActive = [FingerprintMols.FingerprintMol(x) for x in activeMoleculeSet]
fingerprintSetExcluded = [FingerprintMols.FingerprintMol(x) for x in excludedMoleculeSet]
fingerprintSetInactive = [FingerprintMols.FingerprintMol(x) for x in inactiveMoleculeSet]


def tuplemaker(fpSourceSet, fpTargetSet):
    for i in range(len(fpSourceSet)):
        yield (fpSourceSet, fpTargetSet, i)


def getAvgForOneMolecule(tupleInput): # Takes a tuple as input which has(fpSourceSet, fpTargetSet, index)
    fpSourceSet, fpTargetSet, index = tupleInput
    print "Calculating %d out of %d,  %f complete!" %(index, len(fpSourceSet), (100*index/float(len(fpSourceSet))))
    listSim = [DataStructs.FingerprintSimilarity(fpSourceSet[index], fpTargetSet[i]) for i in range(1, len(fpTargetSet))]
    avgforOne = sum(listSim)/float(len(listSim))
    return avgforOne


@pyDec.timeit
def main():
    pool = Pool(8)
    listSimAllIn = pool.map(getAvgForOneMolecule, tuplemaker(fingerprintSetExcluded, fingerprintSetInactive))
    listSimAllAct = pool.map(getAvgForOneMolecule, tuplemaker(fingerprintSetExcluded, fingerprintSetActive))
    listSimAllActIn = pool.map(getAvgForOneMolecule, tuplemaker(fingerprintSetInactive, fingerprintSetActive))

    utilities.dumpToPickle('listSimAllAct', listSimAllAct)
    utilities.dumpToPickle('listSimAllIn',listSimAllIn)
    utilities.dumpToPickle('listSimAllActIn',listSimAllActIn)

    plot = sb.kdeplot(np.array(listSimAllAct), bw=0.005, label = 'Actives and excluded')
    plot = sb.kdeplot(np.array(listSimAllIn), bw=0.005, label = 'Inactives and excluded')
    plot = sb.kdeplot(np.array(listSimAllActIn), bw=0.005, label = 'Actives and inactives')

    plot.set(xlim=(0.1, 0.6))

    plt.show()

main()


