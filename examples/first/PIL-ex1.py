#!/usr/bin/python

from PIL import Image, ImageFilter

parser= argparse.ArgumentParser()
parser.add_argument('img', nargs='?', default="img/vc-xkcd.jpg", help='Image to display')
args= parser.parse_args()

infile= args.img
try:
    original = Image.open(infile)
except:
    print "Unable to load image '%s'" % infile
    exit(1)

print "The size of the %s-Image %s is: %s, Mode %s" % (original.format, infile, original.size, original.mode)

blurred = original.filter(ImageFilter.BLUR)

original.show()
blurred.show()
