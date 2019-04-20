#!/usr/bin/python  
#-*-coding:utf-8-*-

from push_button import *
from clabel import *
from common import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *


class CharacterWidget(QWidget):
	def __init__(self, parent=None):
		super(CharacterWidget, self).__init__()
		self.mouse_press = False
		self.mouse_move = False
		self.current_index = 0 #褰撳墠鍥剧墖涓嬫爣
		self.current_pos_x = 0
		#self.name_list = QStringList()
		self.m_mouseSrcPos = QPoint()
		self.m_mouseDstPos = QPoint()
		self.label_move = False
		self.label_array = [CLabel(), CLabel(), CLabel(), CLabel()] #瀛樺偍鍥剧墖鐨勬暟缁� 

		self.resize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))
		self.setWindowFlags(Qt.FramelessWindowHint)

		self.background_label = QLabel(self) #鑳屾櫙鍥剧墖
		self.background_label.setPixmap(QPixmap("./img/Character/bg_bottom.png"))
		self.background_label.setGeometry(QRect(0, 0, self.width(), self.height()))

		#灏�4寮犲浘鐗囧悎鎴愪竴寮�
		self.pixmap = QPixmap(QSize(self.width() * WINDOW_PAGE_COUNT, WINDOW_HEIGHT)) #
		painter = QPainter(self.pixmap)
		for i  in range(WINDOW_PAGE_COUNT):
			painter.drawImage(QRect(WINDOW_WIDTH * i, 0, WINDOW_WIDTH, WINDOW_HEIGHT), \
				QImage(QString("./img/Character/desktop_%1.png").arg(i)))
		self.total_label = QLabel(self) #鍥剧墖锛堢粨鍚堜綋锛�
		self.total_label.resize(self.pixmap.size())
		self.total_label.setPixmap(self.pixmap)
		self.total_label.move(WINDOW_START_X, WINDOW_START_Y)

		self.close_button = PushButton(self)  #鍏抽棴鎸夐挳
		self.translateLanguage()
		for i in range(WINDOW_BUTTON_COUNT):
			label = CLabel(self)
			label.resize(QSize(155, 45))
			label.setPixmap(QPixmap(QString("./img/Character/btn_%1").arg(i)))
			label.setText(self.name_list[i])
			label.move(8 + i * 170, 319)

			#淇鏃犳硶鍝嶅簲clicked浜嬩欢鐨勯棶棰�
#			self.connect(self.label, SIGNAL("clicked()"), self, SLOT("changeCurrentPage(CLabel())"))
			label.signalLabelPress.connect(self.changeCurrentPage)
			self.label_array[i] = label
		self.label_array[0].setMousePressFlag(False)

		self.close_button.loadPixmap("./img/sysButton/close.png")
		self.close_button.move(self.width() - 52, 0)
		self.connect(self.close_button, SIGNAL("clicked()"), self, SLOT("close()"))


	def translateLanguage(self):
		self.name_list = [u"更换壁纸", u"清理缓存", u"电脑保镖", u"电脑诊断"]
		self.close_button.setToolTip(u"close")

	def mousePressEvent(self, event):
		if(event.button() == Qt.LeftButton):
			self.m_mouseSrcPos = event.pos()
			if(self.m_mouseSrcPos.y() <= 40):
				self.mouse_move = True
			else:
				self.current_pos_x = self.total_label.x()
				self.mouse_press = True
		elif(event.button() == Qt.RightButton):
			if(self.label_move):
				if(self.current_index > 0):
					self.current_index = self.current_index - 1
					self.moveCurrentPage(False) #鍙崇Щ

#杩欓噷鐨勪唬鐮佷細瀵艰嚧浼氭贩涔�
#	def mouseReleaseEvent(self, event):
#		self.xpos = 0
#		if (self.mouse_press):
#			if (self.label_move):
#				self.m_mouseDstPos = event.pos()
#				self.xpos = self.m_mouseDstPos.x() - self.m_mouseSrcPos.x()
#				if(self.xpos > 0):#鍙崇Щ
#					if(self.xpos >= WINDOW_ONEBUTTON_WIDTH):
#						if(self.current_index > 0):
#							self.current_index = self.current_index - 1
#							self.moveCurrentPage(False) #鍙崇Щ
#						else:
#							self.moveCurrentPage(True) #宸︾Щ
#					else:
#						self.moveCurrentPage(True) #宸︾Щ
#				else: #宸︾Щ
#					if(self.xpos <= -WINDOW_ONEBUTTON_WIDTH):
#						if(self.current_index < WINDOW_PAGE_COUNT - 1):
#							self.current_index = self.current_index + 1
#							self.moveCurrentPage(True) #宸︾Щ
#						else:
#							self.moveCurrentPage(False) #鍙崇Щ
#					else:
#						self.moveCurrentPage(False) #鍙崇Щ
#				self.mouse_press = False
#		elif(self.mouse_move):
#			self.mouse_move = False

	
	def changeCurrentPage(self,label):
		
		for i in range(WINDOW_BUTTON_COUNT):
			if(label != self.label_array[i]):
				self.label_array[i].setMousePressFlag(False)
		#鑾峰彇鐐瑰嚮鐨勫浘鏍囦笅鏍�
		index = 0
		for i  in range(WINDOW_PAGE_COUNT):
			if(label == self.label_array[i]):
				index = i
				break	#杩欓噷浠巖eturn鏀逛负break
			
		#鑻ヤ笅鏍囧皬浜庡綋鍓嶄笅鏍囧彸绉伙紝鍚﹀垯宸︾Щ
		if(index < self.current_index):
			while(index != self.current_index):
				self.current_index = self.current_index - 1
				self.moveCurrentPage(False)
		elif(index > self.current_index):
			while(index != self.current_index):
				self.current_index = self.current_index + 1
				self.moveCurrentPage(True)

#	def mouseMoveEvent(self, event):
#		x = 10
#		if(self.mouse_press):
#			if(self.label_move):
#				self.m_mouseDstPos = event.pos()
#				x = self.m_mouseDstPos.x() - self.m_mouseSrcPos.x()
#				self.setLabelMove(False)
#				self.total_label.move(self.current_pos_x + x, WINDOW_START_Y)
#				self.setLabelMove(True)
#		elif(self.mouse_move):
#			self.m_mouseDstPos = event.pos()
#			self.move(event.pos() + self.m_mouseDstPos - self.m_mouseSrcPos) #娉ㄦ剰debug


	def keyPressEvent(self, e):
		if(self.label_move):			
			if e.key() == Qt.Key_Left | e.key() == Qt.Key_Up:
				if(self.current_index > 0):
					self.current_index = self.current_index - 1
					self.moveCurrentPage(False) #鍙崇Щ
					
				elif e.key() == Qt.Key_Down | e.key() == Qt.Key_Right:
					if(self.current_index < WINDOW_PAGE_COUNT - 1):
						self.current_index = self.current_index + 1
						self.moveCurrentPage(True) #宸︾Щ


	def moveCurrentPage(self, direction):
		#鏀瑰彉褰撳墠椤甸潰瀵瑰簲鐨勬寜閽�
		self.changeCurrentButton()

		#鍥剧墖鐨勫嚑涓垎鍓茬偣
		#0-680, 680-1360, 1360-2040, 2040-2720
		#鐪�:鍚戝乏绉�  鍋�:鍚戝彸绉�

		#宸︾Щ鐨勫嚑绉嶅彲鑳芥��,瀵逛簬x鍧愭爣
		#index=0, 灏唋abel绉诲姩鍒�-680*0
		#index=1, 灏唋abel绉诲姩鍒�-680*1
		#index=2, 灏唋abel绉诲姩鍒�-680*2
		#index=3, 灏唋abel绉诲姩鍒�-680*3
		self.setLabelMove(False)
		self.current_pos_x = self.total_label.x() #褰撳墠label鍧愭爣
		self.dest_pos_x = -WINDOW_WIDTH * self.current_index #鐩爣X鍧愭爣
		if(direction):
			if(self.current_pos_x > self.dest_pos_x):
				self.total_label.move(self.current_pos_x - WINDOW_PAGE_MOVE, WINDOW_START_Y)
				self.current_pos_x = self.total_label.x()
				qApp.processEvents(QEventLoop.AllEvents)
		else:
			if(self.current_pos_x < self.dest_pos_x):

				self.total_label.move(self.current_pos_x + WINDOW_PAGE_MOVE, WINDOW_START_Y)
				self.current_pos_x = self.total_label.x()
				qApp.processEvents(QEventLoop.AllEvents)
		self.total_label.move(self.dest_pos_x, WINDOW_START_Y)
		self.setLabelMove(True)

	def changeCurrentButton(self):
		for i in range(WINDOW_BUTTON_COUNT):
			if(i != self.current_index):
				self.label_array[i].setMousePressFlag(False)
			else:
				self.label_array[i].setMousePressFlag(True)

	def setLabelMove(self, enable):
		self.label_move = enable
		
if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	Character = CharacterWidget()
	Character.show()
	sys.exit(app.exec_())
	





