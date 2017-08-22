import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

import determine_expt_inacc as dt
from dipan_utilities import pyDec


def bootstrap_resample(X, n=None):
    """ Bootstrap resample an array_like
    Parameters
    ----------
    X : array_like
      data to resample
    n : int, optional
      length of resampled array, equal to len(X) if n==None
    Results
    -------
    returns X_resamples
    """
    if n == None:
        n = len(X)

    resample_i = np.floor(np.random.rand(n) * len(X)).astype(int)
    X_resample = X[resample_i]
    return X_resample


activelist, inactivelist = dt.inaccAsBoolToList(0, 2)


def bootstrapRandomize(mylist):
    mylist_r = bootstrap_resample(np.array(mylist), len(mylist)/2)
    return mylist_r


def getbalacc():
    activelist_r = bootstrapRandomize(activelist)
    inactivelist_r = bootstrapRandomize(inactivelist)
    balacc = (100 - (
    100 * ((sum(activelist_r) / float(len(activelist_r))) + (sum(inactivelist_r) / float(len(inactivelist_r))))) / 2)
    return balacc


@pyDec.timeit
def main():
    mainlist = []
    for i in range(10):
        mainlist.append(getbalacc())
    plot = sb.kdeplot(np.array(mainlist), bw=0.05)
    plt.show()


if __name__ == "__main__":
    main()
