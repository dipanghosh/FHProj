import csv

def csvToDict(filename):
    reader = csv.reader(open(filename, 'r'))
    dict = {}
    for row in reader:
       _, v, k = row
       dict[k] = v
    return dict

def listToFile(filename, listname):
    with open(filename, 'w') as f:
        for line in listname:
            f.write(line+'\n')

def pullFromDictAndWriteToFIle(yourDict, yourSet, yourFile):
    for id in yourSet:
        try:
            yourFile.write(yourDict[id] + '\n')
        except:
            pass