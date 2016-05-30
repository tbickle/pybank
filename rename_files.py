#!/usr/bin python

####################################################################
#
# Description:
# xxx
#
# USAGE:
# $ cd $HOME/bank
# $ rm ./data/proc_data/lvl0/*
# $ cp ./data/raw_data/* ./data/proc_data/lvl0/
# $ chmod 664 ./data/proc_data/lvl0/*
# $ rm ./data/proc_data/lvl0/currentTransaction*
# $ python ./pybank/rename_files.py
# $ ls -l ./data/proc_data/lvl0/
# $ libreoffice --calc ./data/proc_data/lvl0/201505_0.csv
#
####################################################################

from __future__ import print_function
import sys
import glob
import os

wfile = True

def main() :

	try:

		pwd = "/home/chasemat/bank/data/proc_data/lvl0/"

		files = []
		oldfiles = [f for f in glob.glob(pwd + "*.csv")]
		print(oldfiles)

		# loop through each file individually
		for o in oldfiles:

			curr = o.replace(pwd, "")
			
			if (len(o)>10 and (o[0]+o[1]+o[2])!="201"):	# find files needing to be renamed

				curr = curr.replace("January","01")
				curr = curr.replace("February","02")
				curr = curr.replace("March","03")
				curr = curr.replace("April","04")
				curr = curr.replace("May","05")
				curr = curr.replace("June","06")
				curr = curr.replace("July","07")
				curr = curr.replace("August","08")
				curr = curr.replace("September","09")
				curr = curr.replace("October","10")
				curr = curr.replace("November","11")
				curr = curr.replace("December","12")

				curr = curr[:-9]			# remove junk from tail
				curr = curr[2:]+curr[:2]		# swap month and year
				#curr = pwd + curr + ".csv"
				curr = pwd + curr + "_0.csv"		# level 0 folder

				oldname = o
				newname = curr
				print("Renamed: " + oldname + " --> " + newname)
				if wfile:
					os.rename(oldname, newname)
			else:
				print("Done")
				exit()
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

