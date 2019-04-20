def button2RunFourStep():
#     self.textBrowser.append(step1)
#         self.textBrowser.append(self.my_dir)
#         
#         step2 =  u'step2:执行cuckoo命令...,分析指定目录下的文件'
#         self.textBrowser.append(step2)
#         findAllExeFile(self.my_dir)
#        
#         step3 = u"step3: 提取分析后的json文件..."
#         self.textBrowser.append(step3)
#         #self.textBrowser.append(step3)
#         #mvTOAnalysis()
#         #cuckooToTxt()
#         
#         step4 = u"step4: 准备好测试文件..."
#         self.textBrowser.append(step4)
#         #mvToTest()
#         
#         #step5:运行test.py文件进行测试
#         step5 = u"step5: 测试样本"
#         self.textBrowser.append(step5)
#         #all_predictions = runTest()
#         #self.textBrowser.append(u"分析结果如下: ")
#         #cnt = 1
#         #for i in all_predictions:
#         #    if i == 0:
#          #       self.textBrowser.append(u"第%s个样本为恶意样本..." % cnt)
#           #  else:
#            #     self.textBrowser.append(u"第i个样本为正常样本..." % cnt)
#             #cnt = cnt + 1
    
def button3RunFourStep():
         #step1: choose a directory
         step1 = u'step1:按位置查杀...'
         self.textBrowser.append(step1)
         self.my_dir = QtGui.QFileDialog.getExistingDirectory(self,  u'选择文件夹',  '/')
         self.textBrowser.append(self.my_dir)
         # step2  要把这一步作为一个子进程运行，做完这一步才能继续做step3！: 
         step2 =  u'step2:执行cuckoo命令...,分析指定目录下的文件'
         self.textBrowser.append(step2)
         findAllExeFile(self.my_dir)
         #for file in os.listdir(self.my_dir):
             #print self.my_dir, chardet.detect(self.my_dir)
             #print file, chardet.detect(file)
         #    filename = self.my_dir+"/"+file
             #createSubmit(filename)
          #   self.textBrowser.append(u"分析文件" + filename)
         #step3:将分析后打json文件重命名并放到cuckoo_reports中，运行cuckoo2txt转换为txt文件
         step3 = u"step3: 提取分析后的json文件..."
         self.textBrowser.append(step3)
         #self.textBrowser.append(step3)
         #mvTOAnalysis()
         #cuckooToTxt()
         
         #step4:将txt文件放到test文件夹中以便进行下一步测试
         step4 = u"step4: 准备好测试文件..."
         self.textBrowser.append(step4)
         #mvToTest()
         
         #step5:运行test.py文件进行测试
         step5 = u"step5: 测试样本"
         self.textBrowser.append(step5)
    all_predictions = runTest()
    self.textBrowser.append(u"分析结果如下: ")
    cnt = 1
    for i in all_predictions:
        if i == 0:
            self.textBrowser.append(u"第%s个样本为恶意样本..." % cnt)
        else:
            self.textBrowser.append(u"第i个样本为正常样本..." % cnt)
        cnt = cnt + 1