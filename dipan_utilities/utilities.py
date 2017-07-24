import csv

def csvToDict(filename):
    reader = csv.reader(open(filename, 'r'))
    dict = {}
    for row in reader:
       v, _, k = row
       dict[k] = v
    return dict

def listToFile(filename, listname):
    with open(filename, 'w') as f:
        for line in listname:
            f.write(line+'\n')
