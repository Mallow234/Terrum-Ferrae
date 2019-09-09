import os
import glob
import string
from tempfile import mkstemp
from shutil import move

globalpro = []
conflicts = []

for filename in glob.glob('*.txt'):

  thisfile = open(filename)
  foundflag = False

  while True:
    line = thisfile.readline()

    if foundflag:
      line.rstrip()
      localpro = line.split()

      globalpro.extend(localpro)

      foundflag = False
    if "provinces={" in line:

      foundflag = True

    if not line:
      break

  #localpro = #LINE READ
  #globalpro.append(localpro)
  
  thisfile.close()

conflictset = set([x for x in globalpro if globalpro.count(x) > 1])
conflicts = list(sorted(conflictset))
del conflicts[0]


for filename in glob.glob('*.txt'):

  thisfile = open(filename)
  foundflag = False

  while True:
    line = thisfile.readline()

    if foundflag:
      for x in conflicts:
        if (' ' + x + ' ') in line:
          print( 'sed -i s:' + x + '::g' + ' \"' + filename + '\"')

      foundflag = False
    if "provinces={" in line:

      foundflag = True

    if not line:
      break 
