'''
Created on 30 Jan 2017
@author: dghosh
20 Feb 2017:: Added Multithreading
'''


import os
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import threading
from multiprocessing import Pool
import pathCollections as pc

outputdir = pc.pdbOutputDir
pc.createFolder(outputdir)
def extractSavePdb(outputdir, mol):
    '''
    Takes one molecule at a time from a given moleculeSet, tries to optimise and writes it off as a PDB file
    '''
    molename = mol.GetProp("_Name")
    print molename
    AllChem.EmbedMolecule(mol)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)
    w = Chem.PDBWriter(outputdir + molename + '.pdb')
    w.write(mol)
def minBabel(filename):
    '''
    Minimizes one molecule at a time through OpenBabel
    '''
    print(os.getcwd())
    os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 ./output/' + filename + ' > ./3D_minBabel/' + filename)

pc.createFolder(outputdir)
os.chdir(outputdir)
os.chdir("../")
pc.createFolder('3D_minBabel')
moleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/2276416762553814740.sdf")

#Iterarate over moleculeSet, Generate one thread per molecule. Multithreading in order to process loads quickly...
for mol in moleculeSet:
    t = threading.Thread(target=extractSavePdb, args = (outputdir, mol) )
    t.start()
    
#Generating one thread does not work for Shell, must be run as different processess. Limit the processess to 8(max # of core), employ pool of subworkers to process faster.
pool = Pool(processes=8)
os.chdir(outputdir)
pool.map(minBabel, os.listdir(outputdir))