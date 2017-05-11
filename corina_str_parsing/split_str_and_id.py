'''
Created on 5 May 2017

@author: dghosh
'''
pile = open('/Users/dghosh/Desktop/a.txt').read()
folderpath = '/Users/dghosh/Desktop/Str/'
strList = pile.split('M  END')
x = strList[1]
y = x.split("\n")
#print (y[1].split("\t")[0])

for structure in strList:
    firstLineTemp = structure.split("\n")
    strid = firstLineTemp[1].split("\t")[0]
    file = open(folderpath+strid+".sdf", 'w')
    file.write(structure[1:])
    file.write("M  END")
    file.close()