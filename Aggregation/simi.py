#!/bin/env python

# usage: simi.py (similar|exact) inputfile 
# input file format:
# smiles identifier
#
# Contributing authors:
#   Teague Sterling, Pascal Wassam, Gurgen Turmanian and John Irwin, 2010-2013
#

import xmlrpclib, sys, pprint


def checkAggregators(smi):
    result = server.similarity.getSimilars(smi)
    try:
        similarCount = len(result['aggregators'])

        for r in result['aggregators']:
            if r['similarity'] == 1.0:
                exactMatch = True
                exactmatchref =  r['reference']
        return (similarCount, exactMatch, exactmatchref)

    except:
        pass


lines = file(sys.argv[1]).readlines()
lookups = {}
myfile = sys.argv[2]
for l in lines:
    t = l.split(',')
    smi = t[1]
    id = t[0]
    activity = t[2]
    if len(id) == 0: id = None
    lookups[id] = smi


server_url = "http://advisor.bkslab.org:8080/aggregate_lookup/xml-rpc/"
server = xmlrpclib.ServerProxy(server_url);
similarCount = 0
exactMatch = False
outfile = open(myfile, 'w')
outfile.write('ID, Activity, No. of matches,Exact match, Ref for exact match')
for (id, smi) in lookups.iteritems():
    try:
        checkResult = checkAggregators(smi)
        try:
            outfile.write(id+","+activity+","+",".join(str(x) for x in checkResult)+"\n")
            print id, checkResult
        except:
            outfile.write(id+ ","+ activity +","+ "None"+"\n")
            print id, checkResult
    except:
        pass
outfile.close()
