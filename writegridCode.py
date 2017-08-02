'''
Created on 13 Mar 2017

@author: dghosh
'''
import os
dirName = "/Users/dghosh/Creative Cloud Files/portfolio_site/rome/Rome-web/day1"
os.chdir(dirName)
for filename in os.listdir("."):
    basename = filename[:-8]
    print '<a href="./'+dirName.split("/")[-1]+'/'+basename+'-web.jpg" data-toggle="lightbox" data-gallery="christmasmarket"><figure class="photothumbnail"><img src="./'+dirName.split("/")[-1]+'/thumb/'+basename+'-web-thumb.jpg" alt="'+filename+'" class="center-block"></figure></a>'