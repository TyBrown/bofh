#!/usr/bin/python

import random
import os


bofh_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

with open(bofh_dir + os.path.sep + "bofh.conf", "r") as f:
    lines = [line.strip() for line in f.readlines()]
print "BOFH Excuse of the Day: \t%s" % random.choice(lines)
