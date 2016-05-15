#!/usr/bin python

####################################################################
#
# Description:
# xxx
#
# usage:
# $ cd <>/bank
# $ sudo rm ./proc_data/*
# $ cp ./raw_data/* ./proc_data
# $ sudo chmod 664 ./proc_data/*
# $ rm ./proc_data/currentTransaction*
# $ python3 rename_files.py
#
####################################################################

from __future__ import print_function
import sys
import glob
import os

wfile = True

def main() :

	try:

		pwd = "/home/chasemat/bank/proc_data/"

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
				curr = pwd + curr + ".csv"

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

