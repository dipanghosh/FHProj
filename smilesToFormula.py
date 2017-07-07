'''
Created on 5 Jul 2017

@author: dghosh
'''

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

filepath = 'insert filepath here'
with open(filepath) as f:
    listMol = f.read().splitlines()
outfile = open(filepath[-4:]+'molFolmula.txt', 'w')
for molSmile in listMol:
    mol = Chem.MolFromSmiles(molSmile)
    outfile.write(rdMolDescriptors.CalcMolFormula(mol))
