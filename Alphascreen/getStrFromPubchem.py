from dipan_utilities import utilities
import pubchempy as pcp, pickle
import pandas as pd
inactiveIDList, freqActiveIDList = pickle.load(open("publicdataDump"))

freqActiveDF = (pcp.get_properties('IsomericSMILES', freqActiveIDList, as_dataframe=True))
freqActiveDF = freqActiveDF.rename(columns={'CID': 'externalid', 'IsomericSMILES': 'molecule'})
freqActiveDF['AlphascreenFH'] = 'yes'

inactiveDF = (pcp.get_properties('IsomericSMILES', inactiveIDList, as_dataframe=True))
inactiveDF = inactiveDF.rename(columns={'CID': 'externalid', 'IsomericSMILES': 'molecule'})
inactiveDF['AlphascreenFH'] = 'no'

mergedDF = pd.concat([freqActiveDF, inactiveDF])
utilities.viewTable(mergedDF)
mergedDF.to_excel("mergedMore.xls")

