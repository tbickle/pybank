#!/usr/bin python

####################################################################
#
# Description:
# xxx
#
# USAGE:
# CAUTION...BE SURE NOT TO DELETE DESIRED DATA
# First run rename_file.py process
# Next run compile_data.py process
# Next run assign_cat.py process
# Select user parameters
# $ cd $HOME/bank
# $ rm ./data/proc_data/lvl4/*
# $ python ./pybank/sort_cat.py
# $ ls -l ./data/proc_data/lvl4/
# $ libreoffice --calc ./data/proc_data/lvl4/201505_4.csv
#
####################################################################

from __future__ import print_function
from setuptools import setup
import sys
import glob
import os

##################################################################################
# User Selectable Parameters
##################################################################################

fwrite = 1	# write to file?

##################################################################################

class category() :
	def __init__(self, name, c0, c1, c2, c3, c4, c5, c6) :
		self.name = name		# month filename
		self.c0 = c0
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.c4 = c4
		self.c5 = c5
		self.c6 = c6

##################################################

def main():

	pwd = "/home/chasemat/bank/data/proc_data/lvl3/"
	files = []
	try:
		files = [f for f in glob.glob(pwd + "*.csv")]
		files = [f.replace(pwd, "") for f in files]
		files = [f for f in files if len(f)==12 and (f[0]+f[1]+f[2])=="201"]
	except:
		print("File open error")
		exit()

	#print(files)

	content = []
	data = []
	months = []
	for f in files:
		content = []

		oldfilepath = pwd+f

		newpwd = "/home/chasemat/bank/data/proc_data/lvl4/"
		newfilename = f[-12:-6] + "_4" + f[-4:]
		newfilepath = newpwd+newfilename
	
		cat = category(newfilepath, 0, 0, 0, 0, 0, 0, 0)
		try :
			with open(oldfilepath, "r") as ctnt:
				for c in ctnt:
					content += [c]
		except :
			print("File open error")
			exit()

		tmp = []
		for c in content:
			tmp += c.split("\r\n")

		content = tmp

		for c in content:
			tmp1 = c.split(",")
			try:
				if(len(tmp1)!=3):
					print("???????")
					continue
				else:
					#print(tmp1[0] + "," + tmp1[1] + "," + tmp1[2], end="")
					x = int(tmp1[2])		# category
					if x==0 or x==1 or x==2 or x==3 or x==4 or x==5 or x==6:
						# sort categories
						#print(tmp1[1] + "," + tmp1[2], end="")
						z = float(tmp1[1])	# spent
						if x==0:
							cat.c0 += z
						elif x==1:
							cat.c1 += z
						elif x==2:
							cat.c2 += z
						elif x==3:
							cat.c3 += z
						elif x==4:
							cat.c4 += z
						elif x==5:
							cat.c5 += z
						elif x==6:
							cat.c6 += z
						else:
							print(tmp1[2] + ": Not a category")
							pass
						#print(str(x) + ", " + str(z))
					else:
						print(tmp1[0] + ": Not a category")
						pass
			except:
				print("Error")
				pass

		months += [cat]

		#exit()	# TEST ONLY

##################################################
	if 1:

		for m in months:
			filepath = m.name

			output = ""
			output += "0, " + str(m.c0) + "\n"
			output += "1, " + str(m.c1) + "\n"
			output += "2, " + str(m.c2) + "\n"
			output += "3, " + str(m.c3) + "\n"
			output += "4, " + str(m.c4) + "\n"
			output += "5, " + str(m.c5) + "\n"
			output += "6, " + str(m.c6) + "\n"

			print(filepath)
			print(output)

			if fwrite:
				with open(filepath,"w") as f:
					f.write(output)

##################################################

	exit()

if __name__ == '__main__' :
	main()
	print("Done")

