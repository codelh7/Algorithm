# -*- coding:utf8 -*-
import os
import shutil
import sys

num=154
numP=79
numN=75

#change filename to P_num or N_num and move files to cuckoo_reports
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
			#dire+"/"+dirs+"/reports/reportP_“ + dirs + filename[-5:]
			newfilename=dire+"/"+dirs+"/reports/reportP_"+dirs+filename[-5:]
		else:
			newfilename=dire+"/"+dirs+"/reports/reportN_"+dirs+filename[-5:]
		#print newfilename
#warning: 这里有一个权限问题待解决
		#print "sudo os.rename(" + '\"' + filename + '\",' + '\"' + newfilename + '\"' +")"
		#os.system("sudo os.rename(" + '\"' + filename + '\",' + '\"' + newfilename + '\"' +")")
		print filename, ' ', newfilename
		os.rename(filename, newfilename)
		# move file from old to new
		shutil.move(newfilename, dest)

# move txt files to train or test
def mvTxtfileToTestAndTrain(dire, dest):
	os.chdir(dire)
	for filename in os.listdir(dire):
		if "P" in filename:
			#print filename
			shutil.move(dire+"/"+filename, dest+"/pos/"+filename)
		else:
			#print filename
			shutil.move(dire+"/"+filename, dest+"/neg/"+filename)
		

def mvTOAnalysis():
	mvFileToAnalysis("/home/codelh7/.cuckoo/storage/analyses","/home/codelh7/data/cuckoo_reports")

def mvToTest():
	mvTxtfileToTestAndTrain("/home/codelh7/data/cuckoo_report_txts", "/home/codelh7/data/test")
	
def mvToTrain():
	mvTxtfileToTestAndTrain("/home/codelh7/data/cuckoo_report_txts", "/home/codelh7/data/train")
