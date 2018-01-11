from collections import Counter
import pprint

listofhits = file.readlines(open('/Users/dghosh/Desktop/FreqHitterProject/Fragment/listofhits'))

countofhits = dict(Counter(listofhits))

for i in sorted(countofhits, key=countofhits.get, reverse=True):
    print str.strip(i), countofhits[i]