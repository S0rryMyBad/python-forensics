#!/usr/bin/python2

from PIL import Image

im = Image.open('noosc.png', 'r')
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
print pix_val_flat
