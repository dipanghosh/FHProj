import csv,os
import pickle


desktopDir = '/Users/dghosh/Desktop/'


def csvToSet(filename):
    try:
        reader = csv.reader(open(filename, 'r'))
        mylist = [row[0] for row in reader]
        return set(mylist)
    except:
        pass



def csvToDict(filename):
    reader = csv.reader(open(filename, 'r'))
    dict = {}
    for row in reader:
        v, k, _= row[0], row[1], row[2:]
        dict[k] = v
    return dict


def listToFile(filename, listname):
    with open(filename, 'w') as f:
        for line in listname:
            f.write(str(line)+'\n')


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
    with open(filename, 'wb') as fp:
        pickle.dump(object, fp)

def findCSVFiles(path):
    csvfiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(path)
                 for name in files
                 if name.endswith(("csv"))]
    return csvfiles

def plotVenn(setList):
    from matplotlib_venn import venn3, venn2
    from matplotlib import pyplot as plt
    if len(setList) == 2:
        venn2(setList)
    if len(setList) == 3:
        venn3(setList)
    plt.show()