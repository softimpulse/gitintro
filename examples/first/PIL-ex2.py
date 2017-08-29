#!/usr/bin/python

# Stolen from http://www.pythonforbeginners.com/gui/how-to-use-pillow

from PIL import Image, ImageFilter

infile= "img/Hard_Drive_Cat.jpg"
try:
    original = Image.open(infile)
except:
    print "Unable to load image '%s'" % infile
    exit(1)

print "The size of the original %s-Image %s is: %s, Mode %s" % (original.format, infile, original.size, original.mode)

# Blur the image
blurred = original.filter(ImageFilter.BLUR)
# Display both images
original.show()
blurred.show()