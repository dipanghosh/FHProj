'''
Created on 30 Jan 2017

@author: dghosh
'''
outputdir = '/Users/dghosh/Desktop/output/'
import os
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem

moleculeSet = Chem.SDMolSupplier("/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID1006/1006_active_molecules_combined.sdf")
for mol in moleculeSet:
    molename = mol.GetProp("_Name")
    badFile = outputdir+molename+'.pdb'
    goodFile = outputdir+'/1006Active3D_minBabel/'+molename+'.pdb'
    print molename
    AllChem.EmbedMolecule(mol)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)
    w = Chem.PDBWriter(outputdir+molename+'.pdb')
    w.write(mol)
    #os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+badFile+' > '+goodFile)
for filename in os.listdir(outputdir):
    if filename.ends_with('.pdb'):
        os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+badFile+' > '+goodFile)