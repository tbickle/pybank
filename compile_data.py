from __future__ import print_function
from setuptools import setup
import sys
import glob
import os

##################################################################################

class month() :
	def __init__(self, name, date, ref, payee, addr, cost) :
		self.name = name		# month filename
		self.date = date
		self.ref = ref
		self.payee = payee
		self.addr = addr
		self.cost = cost

class merged() :
	def __init__(self, name, payee, cost):
		self.name = name
		self.payee = payee
		self.cost = cost

def main():

	pwd = "/home/chasemat/bank/proc_data/"
	files = []
	files = [f for f in glob.glob(pwd + "*.csv")]
	files = [f.replace(pwd, "") for f in files]
	files = [f for f in files if len(f)==10 and (f[0]+f[1]+f[2])=="201"]
	#print(files)

##################################################

	content = []
	data = []
	months = []
	for f in files:
		content = []
		m = month(pwd+f, [], [], [], [], [])		# init "month" objects
		try :
			with open(m.name, "r") as ctnt:
				for c in ctnt:
					content += [c]
		except :
			print("File open error")
			exit()

		tmp = []
		for c in content:
			tmp += c.split("\r\n")

		content = tmp[1:]

		for c in content:
			tmp1 = c.split(",")
			try:
				if(len(tmp1)<5):
					print("Comma Error...exiting")
					exit(1)
				if(len(tmp1)>5):
					print("Comma Error...correcting")
					#print(tmp1[0] + "," + tmp1[1] + "," + tmp1[2] + "," + tmp1[3] + "," + tmp1[4] + "," + tmp1[5], end="")
					derp0=tmp1[4]
					derp1=tmp1[5]
					tmp1[2] = tmp1[2] + tmp1[3]
					tmp1[2].replace(","," ")
					tmp1[3]=derp0
					tmp1[4]=derp1
					#print(tmp1[0] + "," + tmp1[1] + "," + tmp1[2] + "," + tmp1[3] + "," + tmp1[4], end="")

				m.ref += [int(tmp1[1])]	# skip if no ref number
				m.date += [tmp1[0]]
				m.payee += [tmp1[2]]
				m.addr += [tmp1[3]]
				m.cost += [float(tmp1[4])]
				#print(tmp1[0] + "," + tmp1[1] + "," + tmp1[2] + "," + tmp1[3] + "," + tmp1[4], end="")

			except:
				pass

		months += [m]

		#break	# TEST ONLY

##################################################

	if 0:
		try:
			for m in months:
				for i in range(len(m.date)):
					print(m.date[i] + "," + str(m.ref[i]) + "," + m.payee[i] + "," + m.addr[i] + "," + str(m.cost[i]))
		except:
			print("Unexpected error:" + sys.exc_info()[0])
			raise

##################################################

	reduced_months = []
	for m in months:
		# search and identify duplicate payees
		merge = []
		log = []

		for i in range(len(m.payee)):

			dupl = False
			# first search if payee has already been logged
			for mm in log:
				if m.payee[i]==mm:
					dupl=True

			# if not logged, proceed to search for duplicates
			if not dupl:
				total = m.cost[i]
				for j in range(len(m.payee)):
					if j<=i:	# make sure we're not double counting
						pass
					else:
						if m.payee[i]==m.payee[j]:
							total += m.cost[j]

				merge += [m.payee[i] + "," + str(total)]
				log += [m.payee[i]]
		
		consolidated = merge

		# MERGED(): making new object of consolidated data
		mm = merged(m.name, [], [])
		for c in consolidated:
			cc = c.split(",")
			mm.payee += [cc[0]]
			mm.cost += [float(cc[1])]

		reduced_months += [mm]

##################################################

	if 1:
		for mm in reduced_months:
			print("")
			print(mm.name)
			for i in range(len(mm.payee)):
				print(mm.payee[i] + "," + str(mm.cost[i]))

	exit()

if __name__ == '__main__' :
	main()
	print("Done")

