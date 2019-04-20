#!/usr/bin/python  
#-*-coding:utf-8-*-
			
from tool_button import ToolButton
from push_button import PushButton
from Qtab1 import *
from Qtab2 import *
from Qtab3 import *
from Qtab4 import *
from Qtab5 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class TitleWidget(QWidget):
	def __init__(self, parent=None):
		super(TitleWidget, self).__init__(parent)
		
		self.skin_button = PushButton(self)
		self.main_menu_button = PushButton(self)
		self.min_button = PushButton(self)
		self.max_button = PushButton(self)
		self.close_button = PushButton(self)
		self.medal_button = QPushButton(self)
		self.button_list = []
		
		#鐗堟湰鏍囬棰滆壊璁剧疆
		self.version_title = QLabel()
		self.version_title.setStyleSheet("color:white")
	
		#璁剧疆鎸夐挳鐨勫浘鐗�
		self.skin_button.loadPixmap("./img/sysButton/skin_button.png")
		self.main_menu_button.loadPixmap("./img/sysButton/main_menu.png")
		self.min_button.loadPixmap("./img/sysButton/min_button.png")
		self.max_button.loadPixmap("./img/sysButton/max_button.png")
		self.close_button.loadPixmap("./img/sysButton/close_button.png")
		
		#璁剧疆鍔熷媼鍥炬爣
		medal_icon = QIcon ("./img/contentWidget/medal_light.png")
		self.medal_button.setIcon(medal_icon)
		self.medal_button.setFixedSize(25, 25)
		self.medal_button.setIconSize(QSize(25, 25))
		self.medal_button.setStyleSheet("background:transparent") #閫忔槑鏄剧ず
	
		self.connect(self.skin_button, SIGNAL("clicked()"), self, SIGNAL("showSkin()"))#涓や釜淇″彿鐨勪簰鐩告縺鍙�
		self.connect(self.main_menu_button, SIGNAL("clicked()"), self, SIGNAL("showMainMenu()"))
		self.connect(self.min_button, SIGNAL("clicked()"), self, SIGNAL("showMin()"))
		self.connect(self.max_button, SIGNAL("clicked()"), self, SIGNAL("showMax()"))
		self.connect(self.close_button, SIGNAL("clicked()"), self, SIGNAL("showClose()")) #closeWidget self, 
	
		title_layout = QHBoxLayout()
		title_layout.addWidget(self.version_title, 0, Qt.AlignVCenter)
		title_layout.addStretch()
		title_layout.addWidget(self.medal_button, 0, Qt.AlignTop)
		title_layout.addWidget(self.skin_button, 0, Qt.AlignTop)
		title_layout.addWidget(self.main_menu_button, 0, Qt.AlignTop)
		title_layout.addWidget(self.min_button, 0, Qt.AlignTop)
		title_layout.addWidget(self.max_button, 0, Qt.AlignTop)
		title_layout.addWidget(self.close_button, 0, Qt.AlignTop)
		title_layout.setSpacing(0)
		title_layout.setContentsMargins(0, 0, 5, 0)
		self.version_title.setContentsMargins(15, 0, 0, 0)
		self.skin_button.setContentsMargins(0, 0, 10, 0)
	
		#string_list = QStringList 
		string_list = ["./img/toolWidget/tiJian.png", "./img/toolWidget/muMa.png", "./img/toolWidget/louDong.png", \
			       "./img/toolWidget/xiTong.png", "./img/toolWidget/qingLi.png"]
	
		button_layout = QHBoxLayout()
# 		self.tabWidget = QTabWidget(self)
# 		
# 		self.tab1 = Qtab1(self)
# 		self.tabWidget.addTab(self.tab1, u"全盘查杀")
# 		
# 		self.tab2 = Qtab2(self)
# 		self.tabWidget.addTab(self.tab2, u"按位置查杀")
# 		
# 		self.tab3 = Qtab3(self)
# 		self.tabWidget.addTab(self.tab3, u"按位置查杀")
# 		
# 		self.tab4 = Qtab4(self)
# 		self.tabWidget.addTab(self.tab4, u"关于我们")
# 		
# 		self.tab5 = Qtab5(self)
# 		self.tabWidget.addTab(self.tab5, u"帮助")
# 		
# 		self.tabWidget.setCurrentIndex(0)
# 		
# 		button_layout.addWidget(self.tabWidget, 0, Qt.AlignBottom)
		self.tool1_button = ToolButton("./img/toolWidget/tiJian.png")
		self.tool2_button = ToolButton("./img/toolWidget/muMa.png")
		self.tool3_button = ToolButton("./img/toolWidget/louDong.png")
		self.tool4_button = ToolButton("./img/toolWidget/xiTong.png")
		self.tool5_button = ToolButton("./img/toolWidget/qingLi.png")
		
		
		self.connect(self.tool1_button, SIGNAL("clicked()"), self, SIGNAL("Qtab1()"))#涓や釜淇″彿鐨勪簰鐩告縺鍙�
		self.connect(self.tool2_button, SIGNAL("clicked()"), self, SIGNAL("Qtab2()"))
		self.connect(self.tool3_button, SIGNAL("clicked()"), self, SIGNAL("Qtab3()"))
		self.connect(self.tool4_button, SIGNAL("clicked()"), self, SIGNAL("Qtab4()"))
		self.connect(self.tool5_button, SIGNAL("clicked()"), self, SIGNAL("Qtab5()"))
  		
 		button_layout.addWidget(self.tool1_button, 0, Qt.AlignBottom)
 		button_layout.addWidget(self.tool2_button, 0, Qt.AlignBottom)
 		button_layout.addWidget(self.tool3_button, 0, Qt.AlignBottom)
 		button_layout.addWidget(self.tool4_button, 0, Qt.AlignBottom)
 		button_layout.addWidget(self.tool5_button, 0, Qt.AlignBottom)

		
		logo_label = QLabel()
		pixmap = QPixmap ("./img/logo.png")
		logo_label.setPixmap(pixmap)
		logo_label.setFixedSize(pixmap.size())
		logo_label.setCursor(Qt.PointingHandCursor)
	
		button_layout.addStretch()
		button_layout.addWidget(logo_label)
		button_layout.setSpacing(8)
		button_layout.setContentsMargins(15, 0, 0, 0)
	
		main_layout = QVBoxLayout()
		main_layout.addLayout(title_layout)
		main_layout.addLayout(button_layout)
		main_layout.setSpacing(0)
		main_layout.setContentsMargins(0, 0, 0, 0)
	
		self.translateLanguage()

		self.setLayout(main_layout)
		self.setFixedHeight(100)
		self.is_move = False
		


	def translateLanguage(self):
	
		self.version_title.setText(u"超星安全卫士 1.0")
		self.skin_button.setToolTip(u"更改皮肤")
		self.main_menu_button.setToolTip(u"主菜单")
		self.min_button.setToolTip(u"最小化")
		self.max_button.setToolTip(u"最大化")
		self.close_button.setToolTip(u"关闭")
	
		
		self.tool1_button.setText(u"全盘查杀")
		self.tool2_button.setText(u"按位置查杀")
		self.tool3_button.setText(u"快速查杀")
		self.tool4_button.setText(u"关于我们")
		self.tool5_button.setText(u"帮助")
		#self.button_list[5].setText(u"optimize")
		#self.button_list[6].setText(u"expert")
		#self.button_list[7].setText(u"software")

	@pyqtSlot()
	def turnPage(self, current_page):	
		current_index = current_page
		print current_index
		for i in range(len(self.button_list)):
			self.tool_button = self.button_list[i]
			if(current_index == i):
				self.tool_button.setMousePress(True)			
			else:
				self.tool_button.setMousePress(False)
		
	

		
if __name__ == '__main__':
	import sys
	
	app = QApplication(sys.argv)
	
	title = TitleWidget()
	title.show()
	
	app.exec_()
		

