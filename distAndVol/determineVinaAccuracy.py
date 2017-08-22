import determineCutoff as dt
import plotVinaener as vi
import csv


perccutoffList = [x * 0.1 for x in range(-110, -29)]

csvfile = open('/Users/dghosh/Desktop/vinaSep.csv', 'w')
csvwriter = csv.writer(csvfile)

for i in perccutoffList:
    falseInactives, trueInactives, falseActives, trueActives, balacc = dt.calcAccuracy(vi.inactiveScoreDict, vi.activeScoreDict, i)
    activeAcc = trueActives / float(len(vi.activeScoreDict))
    inactiveAcc = trueInactives/float(len(vi.inactiveScoreDict))
    csvwriter.writerow((i, trueInactives, falseInactives, inactiveAcc, trueActives, falseActives, activeAcc, balacc))

