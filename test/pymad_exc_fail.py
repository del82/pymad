#! /usr/bin/python

import glob
import os.path
import sys
import StringIO
import urllib

import ao

for p in glob.glob("build/lib.*"):
    sys.path.insert(0, p)

print sys.path

import mad


data = StringIO.StringIO(open("/home/jaq/foo.mp3","r").read())
m = mad.MadFile(data)
print "MadFile returned"
for x in (1,2): pass
print "got here"

