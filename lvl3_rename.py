#!/usr/bin python

####################################################################
#
# Description:
# xxx
#
# USAGE:
# $ cd $HOME/bank
# $ rm ./data/proc_data/lvl3/*
# $ cp ./data/proc_data/lvl2/* ./data/proc_data/lvl3/
# $ chmod 664 ./data/proc_data/lvl3/*
# $ python ./pybank/lvl3_rename.py
# $ ls -l ./data/proc_data/lvl3/
# $ libreoffice --calc ./data/proc_data/lvl0/201505_3.csv
#
####################################################################

from __future__ import print_function
import sys
import glob
import os

wfile = True

def main() :

	try:

		pwd = "/home/chasemat/bank/data/proc_data/lvl3/"

		files = []
		oldfiles = [f for f in glob.glob(pwd + "*.csv")]
		print(oldfiles)

		# loop through each file individually
		for o in oldfiles:

			#curr = o.replace(pwd, "")
			
			#if (len(o)==12 and (o[0]+o[1]+o[2])!="201"):	# find files needing to be renamed

			curr = pwd + o[-12:-6] + "_3" + o[-4:]

			oldname = o
			newname = curr
			print("Renamed: " + oldname + " --> " + newname)
			if wfile:
				os.rename(oldname, newname)
			#else:
				#print("Done")
				#exit()
	except:
		print("ERROR")
		exit(1)
	
#########################################################
	
# end main()

if __name__ == '__main__' :
	main()
	print("Done")

#files = [int(f) for f in files]
#files.sort()
#files = [str(f) for f in files]

