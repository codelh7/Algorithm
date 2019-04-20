# -*- coding:utf8 -*-
import zipfile
import shutil
import os
import sys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#unzip file and extract to directory
def unzip(dire, dest):
	os.chdir(dire)
	for filename in os.listdir(dire):
	    print filename
	    if zipfile.is_zipfile(filename):
				try:
					zipf = zipfile.ZipFile(filename)
					zipf.extractall(dest)
				except RuntimeError:
					zipf = zipfile.ZipFile(filename)
					zipf.extractall(dest, pwd="infected")


#find All exe files and extract all to dest directory
def findExe(dire, dest):
	os.chdir(dire)
	for roots,dirs,filenames in os.walk(dire):
		for filename in filenames:
			if filename[-4:] != ".exe" and filename[-4:] != ".EXE":
				try:				
					os.remove(filename)
				except OSError:
					pass
			else:
				try:
					shutil.move(dire+"/"+filename, dest)
				except:
					pass

		for dir in dirs:
			filepath = dire+"/"+dir
			if os.path.exists(filepath):
				#print filepath			
				unzip(filepath, dest)	
				findExe(filepath, dest)
				shutil.rmtree(filepath)


#rename filename .file to .exe
def rename(dire):
	os.chdir(dire)
	for filename in os.listdir(dire):
		newfilename = filename[:-4] + "exe"
		os.rename(filename, newfilename)


#solve pos zip
def solvePos():
	unzip("/home/codelh7/下载/pos", "/home/codelh7/下载/pos/posExeFile")
	findExe("/home/codelh7/下载/pos/posExeFile", "/home/codelh7/下载/pos/posExeFile")

#solve neg zip
def solveNeg():
	unzip("/home/codelh7/下载/neg", "/home/codelh7/下载/neg/negExeFile")
	findExe("/home/codelh7/下载/neg/negExeFile", "/home/codelh7/下载/neg/negExeFile")
	rename("/home/codelh7/下载/neg/negExeFile")
