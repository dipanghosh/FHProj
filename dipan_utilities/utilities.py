import csv
import pickle

desktopDir = '/Users/dghosh/Desktop/'


def csvToDict(filename):
    reader = csv.reader(open(filename, 'r'))
    dict = {}
    for row in reader:
       v, k, _ = row
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
            print "Failed to transform for " + id


def extractList(idlist, mydict):
    mylist = []
    for id in idlist:
        try:
            mylist.append(mydict[id])
        except KeyError:
            print id + " Key does not exist here!"
    return mylist


def dumpToPickle(filename, object):
    with open(desktopDir+filename, 'wb') as fp:
        pickle.dump(object, fp)