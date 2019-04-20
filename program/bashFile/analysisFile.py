# -*- coding:utf8 -*-
import os
import shutil
import sys

num=154
numP=79
numN=75

#change filename to P_num or N_num
def mvFileToAnalysis(dire, dest):
	os.chdir(dire)
	for dirs in os.listdir(dire):
		filename=dire+"/"+dirs+"/reports/report.json"
		#rename filename P and N
		try:
			valDirs=int(dirs)
		except:
			continue
		if valDirs <= numP:
			newfilename=filename[:6] + "P_" + dirs + filename[-5:]
		else:
			newfilename=filename[:6] + "N_" + dirs + filename[-5:]
		#print newfilename
		os.rename(filename, newfilename)
		# move file from old to new
		shutil.move(newfilename, dest)

def mvTxtfileToTestAndTrain(dire, dest):
	os.chdir(dire)
	for filename in os.listdir(dire):
		if "P" in filename:
			#print filename
			shutil.move(dire+"/"+filename, dest+"/pos/"+filename)
		else:
			#print filename
			shutil.move(dire+"/"+filename, dest+"/neg/"+filename)
		

#mvFileToAnalysis("/home/codelh7/.cuckoo/storage/analyses","/home/codelh7/data/cuckoo_reports")

mvTxtfileToTestAndTrain("/home/codelh7/data/cuckoo_report_txts", "/home/codelh7/data/train")
