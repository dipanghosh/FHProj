from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2
import xlrd
import vennDiagAnalysis as vd
import pandas as pd
from learning import pyDec
import pprint
#print list588342
def printcount(o):
    print len(o)
def extractFromExcel(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
#     get the first worksheet
    sheet = book.sheet_by_index(0)

    x = []
    for rownum in range(sheet.nrows):
        stringVal = str(sheet.cell(rownum, 2))[7:-1]   #Using ExternalID
        try:
            tmp = int(stringVal)
            tmp = str(stringVal)
            #print stringVal
            x.append(tmp)
        except:
            try:
                x.append((stringVal[:-1]))
            except:
                print stringVal
    
    x = set(x)
    return x

def sanitizeExcel(d):
    d = str(d)
    print d[7:-2]
    return d[7:-2]
#@pyDec.timeit
def readtoDict(path, col1, col2, *args):
    pass
    book = xlrd.open_workbook(path)
#     get the first worksheet
    sheet = book.sheet_by_index(0)
    x={}
    for rownum in range(sheet.nrows):
        externalID = sanitizeExcel(sheet.cell(rownum, col1))
        activity = sanitizeExcel(sheet.cell(rownum, col2))   
        x[externalID] = activity
    return x
    
    
def addThree(a,b,c):
    result = ((a&b)|(b&c)|(c&a))
    return result
def writeTofile(obj, path):
    with open(path, 'w') as f:
        for line in obj:
            f.write(line)
            f.write('\n')
basepath = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/MachineLearning/incorrect/'
act_411_i = extractFromExcel(basepath+'411_actives_incorrect.xls')
act_1006_i = extractFromExcel(basepath+'1006_actives_incorrect.xls')
act_588342_11_5_i = extractFromExcel(basepath+'588342_11_5_actives_incorrect.xls')
act_588342_i = extractFromExcel(basepath+'588342_actives_incorrect.xls')
inact_411_i = extractFromExcel(basepath+'411_inactives_incorrect.xls')
inact_1006_i = extractFromExcel(basepath+'1006_inactives_incorrect.xls')
inact_588342_i = extractFromExcel(basepath+'588342_inactives_incorrect.xls')
inact_588342_11_5_i = extractFromExcel(basepath+'588342_11_5_inactives_incorrect.xls')
dict_588342 = readtoDict('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID588342/AID_588342_datatable_all.xlsx', 2, 21)
atleastTwice = addThree(inact_1006_i, inact_411_i, inact_588342_i)
atleastTwiceAct = addThree(act_1006_i, act_411_i, act_588342_i)
writeTofile(atleastTwice, basepath+'inactiveTwice')
writeTofile(atleastTwiceAct, basepath+'activeTwice')
#vd.printcount(atleastTwiceAct)
#print test1
#print(len(hitForThree))
#print(len(uniquein588342))
#print(len(onlyin1006))

pprint.pprint(dict_588342)

print inact_588342_i
for i in inact_588342_i:
    try:
        print dict_588342[i]
    except:
        print i+'failed'

#venn3([inact_411_i, inact_1006_i, inact_588342_i])
#plt.show()
#venn3([act_411_i, act_1006_i, act_588342_i])
#venn2([vd.reproducibleMembers, set.union(act_411_i, act_1006_i, act_588342_i)])
#plt.show()
#venn2([vd.active588342Inactive1006Inactive411, inact_588342_11_5_i])
#plt.show()
#venn3([set(list1006), set(list588342), set(list411)], ('AID1006', 'AID588342', 'AID411'))
#plt.show()