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
            print ("Failed to transform for " + id)


def extractList(idlist, mydict):
    mylist = []
    for id in idlist:
        try:
            mylist.append(mydict[id])
        except KeyError:
            print (id + " Key does not exist here!")
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

def getSingleStrFromPubchem(SID):
    import pubchempy as pcp
    return pcp.Substance.from_sid(SID).standardized_compound.isomeric_smiles

def getSmilesFromPubchem(CIDList):
    import requests
    import pandas as pd
    cid_chunks = list(chunks(CIDList, 200))
    dflist = []
    for chunk in cid_chunks:
        cids = ",".join(chunk)
        response = requests.get ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+cids+"/property/CanonicalSMILES/CSV")
        smiles_strings = response.content.decode("utf-8").split("\n")
        df = pd.DataFrame([sub.replace('\"',"").split(",") for sub in smiles_strings[1:len(smiles_strings)-1]], columns=["CID", "SMILES"])
        dflist.append(df)
    return pd.concat(dflist)


def pcp_getSmilesFromPubchem(CIDList, renameDict = {}, addCol = {}):
    import pubchempy as pcp
    smilesDF = (pcp.get_properties('IsomericSMILES', CIDList, as_dataframe=True))
    if renameDict:
        smilesDF = smilesDF.rename(columns=renameDict)
        smilesDF.drop(smilesDF.index[0])
    if addCol:
        for i in addCol.keys():
            smilesDF[i] = addCol[i]

    return smilesDF


def viewTable(table):
    import webbrowser
    # Create a web page view of the data for easy viewing
    html = table.to_html()

    # Save the html to a temporary file
    with open("data.html", "w") as f:
        f.write(html)

    # Open the web page in our web browser
    full_filename = os.path.abspath("data.html")
    webbrowser.open("file://{}".format(full_filename))

def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]