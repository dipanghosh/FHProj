'''
Created on 30 Jan 2017

@author: dghosh
'''
import os
#import chimera_run
resultDir = "/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/finalVinaOutput/"
if not os.path.exists(resultDir):
    os.makedirs(resultDir)
inputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaDockPrep/'
pdbDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaprepDonePdb/'
vinaDoneDir = "/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaDoneDir/"
if __name__ == "__main__":
    for filename in os.listdir(pdbDir):
        #print filename[:-4]
        os.system('~/Desktop/Tools/vina --cpu 8 --receptor '+inputdir+filename[:-4]+'.receptor.pdbqt --ligand '+inputdir+filename[:-4]+'.ligand.pdbqt --out '+resultDir+filename[:-4]+'.ouput.pdbqt --config '+inputdir+filename[:-4]+'.conf')
        os.rename(pdbDir+filename, vinaDoneDir+filename)
        print ("\n\n\n"+pdbDir+filename+" moved to "+vinaDoneDir+filename+"\n\n\n")