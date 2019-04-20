#!/usr/bin/python  
#-*-coding:utf-8-*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class ChangeSkinWidget(QWidget):
	skin = pyqtSignal()
	def __init__(self,parent = None):
		super(ChangeSkinWidget,self).__init__(parent)
		self.setFixedSize(140, 160)
		self.mouse_press = False
		self.mouse_enter = False
		#self.pixmap = QPixmap()
		self.pixmap_name = ""

		self.skin_label =  QLabel() #鏄剧ず鐨偆
		self.skin_name_label =  QLabel() #鏄剧ず鐨偆鍚嶇О
		self.download_count_label =  QLabel() #鏄剧ず涓嬭浇娆℃暟
		self.use_skin_button =  QPushButton() #浣跨敤姝ょ毊鑲ゆ寜閽�
		self.setCursor(Qt.PointingHandCursor)

		#淇杩欓噷瀛樺湪鏃犳硶瑙ｉ噴鐨勬儏鍐�
		#Could not parse stylesheet of widget 0x1df35a8
		self.use_skin_button.setStyleSheet("border-radius:3px;border:1px solid rgb(180, 190, 200);color:rgb(70, 70, 70);background:transparent")
		self.skin_label.setScaledContents(True)
		self.skin_label.setFixedSize(100, 65)
		self.use_skin_button.setFixedSize(85, 25)

		self.background_layout =  QVBoxLayout()
		self.background_layout.addWidget(self.skin_label, 0, Qt.AlignCenter)
		self.background_layout.addWidget(self.skin_name_label, 0, Qt.AlignCenter)
		self.background_layout.addWidget(self.download_count_label, 0, Qt.AlignCenter)
		self.background_layout.addWidget(self.use_skin_button, 0, Qt.AlignCenter)
		self.background_layout.setSpacing(5)
		self.background_layout.setContentsMargins(0, 10, 0, 10)

		self.setLayout(self.background_layout)
		self.skin.connect(self.changeSkin)

		self.translateLanguage()
	
	
	
	def changeSkin(self, pixmap_name,  skin_name,  download_count):
		self.background_name = pixmap_name + "_big.png"
		self.pixmap_name = self.background_name

	#鏇存敼鐨偆鑳屾櫙
		#self.pixmap()
		self.skin_label.setPixmap(QPixmap(self.background_name))

	#鏇存敼鐨偆鍚嶇О
		self.skin_name_label.setText(skin_name)

	#鏇存敼涓嬭浇娆℃暟
		self.download_count_label.setText(u"download count:" + download_count)

	def translateLanguage(self):
		self.use_skin_button.setText(u"use skin")

	def paintEvent(self,event):
		if(self.mouse_enter):
			#缁樺埗杈规
			painter = QPainter(self)
			pen = QPen(QColor(210, 225, 230))
			painter.setPen(pen)
			painter.drawRoundRect(0,0,self.width()-1, self.height()-1, 5, 5)

	def mousePressEvent(self,event):
		#鍙兘鏄紶鏍囧乏閿Щ鍔ㄥ拰鏀瑰彉澶у皬
		if(event.button() == Qt.LeftButton):
			self.mouse_press = True
			self.emit(SIGNAL("skin"),self.pixmap_name)

	def mouseReleaseEvent(self,event):
		self.mouse_press = False

	def enterEvent(self,event):
		self.mouse_enter = True
		self.update()

	def leaveEvent(self,event):
		self.mouse_enter = False
		self.update()
'''鍋氫竴涓猰ain鍑芥暟瀵圭▼搴忕殑杩愯骞舵病鏈夊疄闄呯殑鎰忎箟锛屽彧鏄负浜嗘柟渚挎祴璇�'''
if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	
	skin = ChangeSkinWidget()
	skin.show()
	
	sys.exit(app.exec_())
