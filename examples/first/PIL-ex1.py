#!/usr/bin/python

from PIL import Image, ImageFilter

infile= "img/Hard_Drive_cat.jpg"
try:
    original = Image.open(infile)
except:
    print "Unable to load image '%s'" % infile
    exit(1)

print "The size of the %s-Image %s is: %s, Mode %s" % (original.format, infile, original.size, original.mode)

