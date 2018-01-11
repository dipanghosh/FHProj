import os

filepath = "/Users/dghosh/Creative Cloud Files/portfolio_site/galleries/flowers"

for filename in os.listdir(filepath):
    thumbnailname = filename[:-8] + "-thumb.jpg"
    print '<a href="flowers/%s" data-toggle="lightbox" data-gallery="christmasmarket" class ="imageitem"> <img src = "flowers/thumb/%s" alt = "Flower Photography, Dipan Ghosh"/> </a>'%(filename, thumbnailname)
