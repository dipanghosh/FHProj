'''
Created on 13 Mar 2017

@author: dghosh
'''
import os

dirName = "/Users/dghosh/Creative Cloud Files/portfolio_site/galleries/salzburg"
os.chdir(dirName)
for filename in os.listdir("."):
    basename = filename[:-4]
    print '<a href="./' + dirName.split("/")[-1] + '/' + basename + \
          '.jpg" data-toggle="lightbox" data-gallery="christmasmarket">' \
          '<figure class="photothumbnail"><img src="./' + dirName.split("/")[-1] + \
          '/thumb/' + basename + '-thumb.jpg" alt="' + filename + '" class="center-block">' \
                                                                      '</figure></a>'
