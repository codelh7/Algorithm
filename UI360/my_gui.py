# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from myPackage.mvFile import *
from myPackage.analysisFile import *
from myPackage.cuckoo2txt import *
from myPackage.test import *
from myPackage.train import *
from myPackage.mvFile import *

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
from Ui_my_gui import Ui_MainWindow
import os, shutil
import sys
import chardet
import time
reload(sys)
sys.setdefaultencoding('utf8')
 
class DeleteFiles(object):
    def __init__(self, pathDir):
        self.pathDir = pathDir
 
    def delete_files(self):
        os.chdir(self.pathDir) 
        fileList = list(os.listdir()) 
        for file in fileList: 
            if os.path.isfile(file): 
                os.remove(file) 
                print("delete successfully")
            else: 
                shutil.rmtree(file)
 

def createSubmit(path):
    import requests
    REST_URL = "http://localhost:8090/tasks/create/file"
    SAMPLE_FILE = unicode(path).encode('utf8')
    #print SAMPLE_FILE, chardet.detect(SAMPLE_FILE)
    HEADERS = {"Authorization": "Bearer S4MPL3"}
    
    with open(SAMPLE_FILE, "rb") as sample:
        files = {"file": ("temp_file_name", sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files)
    # Add your code to error checking for r.status_code.
    task_id = r.json()["task_id"]


def findAllExeFile(dire):  
    analysisList = []
    os.chdir(dire)
    for roots,dirs,filenames in os.walk(unicode(dire)):
        for filename in filenames:
            #print filename
            if filename[-4:] != ".exe" and filename[-4:] != ".EXE":
                pass
            else:
                try:
                    newfilename = dire + "/" + filename
                    analysisList.append(newfilename)
                    #createSubmit(newfilename)
                    ui.textBrowser.append(u"分析文件" + newfilename)
                    #print u"分析文件" + newfilename
                except:
                    pass

        for dir in dirs:
            filepath = dire+"/"+dir
            if os.path.exists(filepath):
                #print filepath               
                analysisList.append(findAllExeFile(filepath))
    
    return analysisList            
                
def runFourStep(self):
    # step1: choose a directory  
    self.textBrowser.append(self.my_dir)
    # step2  要把这一步作为一个子进程运行，做完这一步才能继续做step3！: 
    step2 =  u'step2:执行cuckoo命令...,分析指定目录下的文件'
    self.textBrowser.append(step2)
    analysisList = findAllExeFile(self.my_dir)
    #step3:将分析后打json文件重命名并放到cuckoo_reports中，运行cuckoo2txt转换为txt文件
    for filename in analysisList:
        createSubmit(filename)
        path1 = "/home/codelh7/.cuckoo/storage/analyses"
        print os.listdir(path1)
        time.sleep(300)
        step3 = u"step3: 提取分析后的json文件..."
        self.textBrowser.append(step3)
        mvTOAnalysis()
        path2 = "/home/codelh7/data/cuckoo_reports"
        cuckooToTxt()
        path3 = "/home/codelh7/data/cuckoo_report_txts"
        #step4:将txt文件放到test文件夹中以便进行下一步测试
        step4 = u"step4: 准备好测试文件..."
        self.textBrowser.append(step4)
        mvToTest()
        path4 = "/home/codelh7/data/test/pos"
        #step5:运行test.py文件进行测试
        step5 = u"step5: 测试样本"
        self.textBrowser.append(step5)
        all_predictions = []
        all_predictions = runTest()
        self.textBrowser.append(u"分析结果如下: ")
        cnt = 1
        #print all_predictions
        for i in all_predictions:
            if i == 0:
                self.textBrowser.append(u"%s为恶意样本..." % filename)
            else:
                self.textBrowser.append(u"%s为正常样本..." % filename)
                
        paths = [path1, path2, path3, path4]
        #for path in paths:
        for root, dirs, files in os.walk(path1, topdown=False):
            for name in files:
                if name != 'latest':
                    os.remove(os.path.join(root, name))
            for name in dirs:
                if name != 'latest':
                    os.rmdir(os.path.join(root, name))
              
        for root, dirs, files in os.walk(path2, topdown=False):
            for name in files:
                    os.remove(os.path.join(root, name))
            for name in dirs:
                    os.rmdir(os.path.join(root, name))
              
        for root, dirs, files in os.walk(path3, topdown=False):
            for name in files:
                    os.remove(os.path.join(root, name))
            for name in dirs:
                    os.rmdir(os.path.join(root, name))
                    
        for root, dirs, files in os.walk(path4, topdown=False):
            for name in files:
                    os.remove(os.path.join(root, name))
            for name in dirs:
                    os.rmdir(os.path.join(root, name))
                        
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        step1 = u"step1:全局查杀"
        self.textBrowser.append(step1)
        self.my_dir = "/"
        runFourStep(self)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # 快速查杀 : 指定关键位置进行查杀  这里只查杀usr目录
        step1 = u'step1:按位置查杀...'
        self.textBrowser.append(step1)
        self.my_dir = '/bin'
        runFourStep(self)
        
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        step1 = u'step1:按位置查杀...'
        self.textBrowser.append(step1)
        self.my_dir = QtGui.QFileDialog.getExistingDirectory(self,  u'选择文件夹',  '/')
        
        runFourStep(self)
                
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
