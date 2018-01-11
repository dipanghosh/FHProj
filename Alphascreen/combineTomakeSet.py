baseDir = '/Users/dghosh/Desktop/FreqHitterProject/Alphascreen/Data/'

from dipan_utilities import utilities

basedata = utilities.csvToDict(baseDir+'basedata.csv')
genFH = utilities.csvToDict(baseDir+'gen-FH.csv')

basedataset = set(basedata.keys())
genFHSet = set(genFH.keys())

notFH = (basedataset-genFHSet)

utilities.listToFile(baseDir+'notFH.csv', notFH)
utilities.listToFile(baseDir+'genFH.csv', genFHSet)