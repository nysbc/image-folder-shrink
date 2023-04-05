#!/usr/bin/env python
'''
This script reduces the size of leginon image folder when there
are dose-weighted image presence.
This is done by shrinking unaligned image to 8x8 array that
retains mean and standard deviation of the original mrc image.
It also remove non dose weighted aligned file and replaces
it with a soft link to the dose-weighted version.
'''
import numpy
import sys
import os
import glob
from pyami import mrc

def repairFolderShrink(folderpath, force=False):
	cwd = os.getcwd()
	if not os.path.isdir(folderpath):
		print('Not a directory, bypassed')
	dwmrcs = glob.glob(os.path.join(folderpath,'*DW.mrc'))
	os.chdir(folderpath)
	for dw in dwmrcs:
		print('Processing %s' % dw)
		# use relative path so that it does not lose the link if the directory
		# is moved.
		dw = os.path.basename(dw)
		aligned = dw.replace('-DW.mrc','.mrc')
		if os.path.islink(aligned) and (force or not os.path.isfile(aligned)):
			os.remove(aligned)
			os.symlink(dw, aligned)
			print('  %s is now linked to the local %s' % (aligned, dw))
	# change back to working directory
	os.chdir(cwd)

if __name__=='__main__':
	if len(sys.argv) < 2:
		print('Usage: Provide a leginon image data folder name, please')
		print('add option force to force redoing all links regardlessly')
		sys.exit(1)
	if len(sys.argv) == 3 and sys.argv[2] == 'force':
		force = True
	else:
		force = False
	repairFolderShrink(sys.argv[1], force)

