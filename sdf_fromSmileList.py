'''
Created on 1 Mar 2017

@author: dghosh
'''
import os
from rdkit import Chem
from rdkit.Chem import AllChem

with open('/Users/dghosh/Desktop/PKR1Project/molecules_smiles.txt') as f:
    smilesList = f.read().splitlines()
moleculeList = []
for smile in smilesList:
    m = Chem.MolFromSmiles(smile)
    #m2.SetProp("_Name","cyclobutane")
    AllChem.EmbedMolecule(m)
    #print(Chem.MolToMolBlock(m))
    moleculeList.append(m)
w = Chem.SDWriter('/Users/dghosh/Desktop/PKR1Project/molecules.sdf')
for m in moleculeList: w.write(m)