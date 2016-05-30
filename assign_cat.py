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
# Select user parameters
# $ cd $HOME/bank
# $ rm ./data/proc_data/lvl2/*
# $ python ./pybank/assign_cat.py
# $ ls -l ./data/proc_data/lvl2/
# $ libreoffice --calc ./data/proc_data/lvl2/201505_2.csv
#
"""
Current categories:
1)	   FOOD: restaurant, grocery, pet food
2)	    CAR: gas, insur, repair, etc
3)	  BILLS: rent, internet, etc
4)	 HEALTH: workout, dental, doctor, vet
5)	 TRAVEL: plane, uber, hotel
6)	CLOTHES: rei, american apparel
5)	ELSE	
"""
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

Cat1 = ["food","restaurant","thai","india","cafe","brew","coffee",
	"grocery","lounge"," ale ","beer","store","wholefds","mexican",
	"middle east","caffe","chicken","ethiopian","market","grill",
	"pollo","table","tavern","burger","liquor","taco","baguette",
	"boba","tea","petco","trader","sandwich","pet ","cream","vons",
	"starbucks"]
Cat2 = ["car ","auto","gas","fuel","insurance","repair","exxon","chevron","shell"]
Cat3 = ["internet","cable"]
Cat4 = ["bikram","pilates","dental","vca"]
Cat5 = ["fly","airline","uber","hampton inn","airport","delta"]
Cat6 = ["rei ","apparel"]

class Categories():
	def __init__(self, fname, out):
		self.fname = fname
		self.out = out

##################################################

def main():

	pwd = "/home/chasemat/bank/data/proc_data/lvl1/"
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
	output = ""
	months = []
	for f in files:

		cat = Categories("","")

		oldfilepath = pwd+f

		newpwd = "/home/chasemat/bank/data/proc_data/lvl2/"
		newfilename = f[-12:-6] + "_2" + f[-4:]
		newfilepath = newpwd+newfilename
		
		#print(newfilepath)
		cat.fname = newfilepath

		content = []
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
		#print(content)

		blerf = ""
		total = 0
		found = 0
		nfound = 0

		for c in content:

			blerf = c.lower()		# lowercase contents in each line
			ncat = 0

			for cc in Cat1:
				if cc in blerf:
					if ncat==0:
						ncat = 1
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()
			for cc in Cat2:
				if cc in blerf:
					if ncat==0:
						ncat = 2
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()
			for cc in Cat3:
				if cc in blerf:
					if ncat==0:
						ncat = 3
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()
			for cc in Cat4:
				if cc in blerf:
					if ncat==0:
						ncat = 4
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()
			for cc in Cat5:
				if cc in blerf:
					if ncat==0:
						ncat = 5
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()
			for cc in Cat6:
				if cc in blerf:
					if ncat==0:
						ncat = 6
						#print("Cat" + str(cat) + ": " + cc)
						break
					else:
						ncat = -1
						print(" Err: " + cc)
						exit()

			if ncat==0:
				nfound += 1
				#print("Category not found")
			else:
				found += 1
			total += 1

			cat.out += c[:-1] + "," + str(ncat) + "\n"

		months += [cat]

		print(oldfilepath)
		print("======================")
		print("    Found: " + str(found))
		print("Not found: " + str(nfound))
		print("    Total: " + str(total))
		print("")

##################################################

	if 1:
		for m in months:

			filepath = m.fname
			output = m.out

			#print(filepath)
			#print(output)

			if fwrite:
				with open(filepath,"w") as f:
					f.write(output)
	exit()

if __name__ == '__main__' :
	main()
	print("Done")

