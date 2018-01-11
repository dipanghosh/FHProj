import os,pickle, re
import pubchempy as pb
from mineTextData import assaydata
import headless
import csv
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/bigAssayOthers/'
outfile  = open(dataDir+"assayDesc.txt", 'w')
dataDir1 = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/'
listofassay = pickle.load(open(dataDir1 + "datainfo.pkl", "r"))



def getRecord():
    try:
        outfile.write(myfile[:-4] + " , " + str(pb.Assay.from_aid(myfile[:-4]).record) + "\n")
    except (pb.BadRequestError):
        pass

def processProtocolText(text):
    found = [sentence + '.' for sentence in text.split('.') if 'concentration' in sentence]
    return found

def processFromwebpage(AID):
    aid = AID[:-4]
    try:
        protocolText = headless.getAssayProtocol(aid)
        imp = processProtocolText(protocolText)
        print " , ".join(map(str, [aid, imp]))
    except (AttributeError):
        print "Unable to locate protocol for AssyID "+aid

def floatify(mylist):
    flList = []
    for i in mylist:
        try:
            flList.append(float(i))
        except(ValueError):
            pass
    return flList

concDict = {}
for csvfile in os.listdir(dataDir1+'AllData/'):
    #print csvfile
    reader = csv.reader(open(dataDir1+'AllData/'+csvfile))
    header = next(reader)
    # print header
    pattern = "(?<=at).*?(?=uM)"
    pattern2 = "(?<=@).*?(?=uM)"
    pattern3 = "(?<=SCORE_).*?(?=uM)"
    list1 =  [str.strip(re.findall(pattern, i)[0], '_') for i in header if re.findall(pattern, i)]
    list2 =  [re.findall(pattern2, i)[0] for i in header if re.findall(pattern2, i)]
    list3 =  [re.findall(pattern3, i)[0] for i in header if re.findall(pattern3, i)]
    cncList = floatify(list1+list2+list3)
    if(len(cncList)):
        concDict[int(csvfile[:-4])] = cncList
    else:
        processFromwebpage(csvfile)

