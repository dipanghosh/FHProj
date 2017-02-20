'''
Created on 30 Jan 2017

@author: dghosh
extractSavePdb






'''
outputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/output/'
import os
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import threading
def extractSavePdb(outputdir, mol):    
        molename = mol.GetProp("_Name")
        #badFile = outputdir + molename + '.pdb'
        #goodFile = outputdir + '/3D_minBabel/' + molename + '.pdb'
        print molename
        AllChem.EmbedMolecule(mol)
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        AllChem.UFFOptimizeMolecule(mol)
        w = Chem.PDBWriter(outputdir + molename + '.pdb')
        w.write(mol)
    
os.mkdir(outputdir)
os.chdir(outputdir)
os.chdir("../")
os.mkdir('3D_minBabel')
moleculeSet = Chem.SDMolSupplier("/Users/dghosh/Downloads/2276416762553814740.sdf")
#print("There are %d CPUs on this machine" % mp.cpu_count())

for mol in moleculeSet:
    t = threading.Thread(target=extractSavePdb, args = (outputdir, mol) )
    t.start()
    
    #os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+badFile+' > '+goodFile)
for filename in os.listdir(outputdir):
    #print filename[-4:]
    if filename[-4:]=='.pdb':
        os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+filename+' > ../3D_minBabel/'+filename)