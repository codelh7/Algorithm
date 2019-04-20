#!/usr/bin/python  
#-*-coding:utf-8-*-

from title_widget import *
from content_widget import *
from system_tray import *
from about_us import *
from main_menu import *
from character_widget import *
from setting_dialog import *
from  skin_widget import *
from Qtab1 import *
from Qtab2 import *
from Qtab3 import *
from Qtab4 import *
from Qtab5 import *
import util

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *


class MainWidget(QWidget):
	closeWidget = pyqtSignal()
	
	def __init__(self, parent=None):
		super(MainWidget, self).__init__()
		self.location = QRect()
		
		self.title_widget = TitleWidget(self) #
		self.title_widget.setFixedHeight(100)
		
		self.content_widget = ContentWidget(self) #
		
# 		self.Qtab1 = Qtab1(self)
# 		self.Qtab2 = Qtab1(self)
# 		self.Qtab3 = Qtab3(self)
# 		self.Qtab4 = Qtab4(self)
# 		self.Qtab5 = Qtab5(self)
		
		self.system_tray = SystemTray(self) #
		self.setting_dialog = SettingDialog(self) #
		self.character_widget = CharacterWidget(self) #
		self.about_us_dialog = AboutUsDialog(self) #
		self.skin_name = QString("./img/skin/17_big.png") #
		self.main_menu = MainMenu() #
		self.skin_widget = SkinWidget() #
		self.setMinimumSize(900, 600) #
		
		self.setWindowIcon(QIcon("./img/safe.ico"))#

		self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)#
		self.location = self.geometry() #
		self.closeWidget.connect(self.close)#-----------------------close
		
		self.is_max = False

		self.center_layout = QVBoxLayout()
		self.center_layout.addWidget(self.content_widget)
		self.center_layout.setSpacing(0)
		self.center_layout.setContentsMargins(1, 0, 1, 1)

		main_layout = QVBoxLayout()
		main_layout.addWidget(self.title_widget)
		main_layout.addLayout(self.center_layout)
		main_layout.setSpacing(0)
		main_layout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(main_layout)
		
		self.connect(self.title_widget, SIGNAL("showAboutUs()"), self, SLOT("showAboutUs()"))
		self.connect(self.title_widget, SIGNAL("showSkin()"), self, SLOT("showSkinWidget()"))
		self.connect(self.title_widget, SIGNAL("showMainMenu()"), self, SLOT("showMainMenu()"))
		self.connect(self.title_widget, SIGNAL("showMax()"), self, SLOT("showMax()"))
		self.connect(self.title_widget, SIGNAL("showMin()"), self, SLOT("showMinimized()"))
		self.connect(self.title_widget, SIGNAL("showClose()"), self, SLOT("showClose()")) #hide()#-----------------------close
		
		self.connect(self.title_widget, SIGNAL("Qtab1()"), self, SLOT("changeQtab1()"))
		self.connect(self.title_widget, SIGNAL("Qtab2()"), self, SLOT("changeQtab2()"))
		self.connect(self.title_widget, SIGNAL("Qtab3()"), self, SLOT("changeQtab3()"))
		self.connect(self.title_widget, SIGNAL("Qtab4()"), self, SLOT("changeQtab4()"))
		self.connect(self.title_widget, SIGNAL("Qtab5()"), self, SLOT("changeQtab5()"))

		#self.connect(self.content_widget, SIGNAL("showAboutUs()"), self, SLOT("showAboutUs()"))

		self.connect(self.main_menu, SIGNAL("showSettingDialog()"), self, SLOT("showSettingDialog()"))
		self.connect(self.main_menu, SIGNAL("showCharacter()"), self, SLOT("showCharacter()"))
		self.connect(self.main_menu, SIGNAL("showAboutUs()"), self, SLOT("showAboutUs()"))

		self.connect(self.skin_widget, SIGNAL("changeSkin()"), self, SLOT("changeSkin()"))
		self.connect(self.system_tray, SIGNAL("activated()"), self, SLOT("iconIsActived()"))
		self.connect(self.system_tray, SIGNAL("showClose()"), self, SLOT("showClose()"))#-----------------------close

		self.system_tray.show()
		
		self.pixmap = QPixmap()
		self.pixmap.load(self.skin_name)
		

	@pyqtSlot()
	def showClose(self):
		self.close()

	def paintEvent(self, event):# QPaintEvent *
		
		painter = QPainter(self)
		painter.drawPixmap(self.rect(), self.pixmap)
		painter.end()
		
		painter2 = QPainter (self)
		painter2.setPen(Qt.gray)
		painter2.drawPolyline(QPointF(0, 100), QPointF(0, self.height() - 1), QPointF(self.width() - 1, self.height() - 1), QPointF(self.width() - 1, 100))
		painter2.end()
	
	@pyqtSlot()	
	def showMax(self):
		#淇鏈夐棶棰樼殑鏈�澶у寲
		if not self.isMaximized():
			self.showMaximized()
		else:
			self.showNormal()
	
	@pyqtSlot()	
	def showSkinWidget(self):
		self.skin_widget.show()
	
	@pyqtSlot()	
	def showMainMenu(self):
		p = self.rect().topRight() #QPoint
		p.setX(p.x() - 150)
		p.setY(p.y() + 22)
		self.main_menu.exec_(self.mapToGlobal(p))
	
	@pyqtSlot()	
	def iconIsActived(self, reason): #QSystemTrayIcon.ActivationReason 

		if reason == QSystemTrayIcon.Trigger:
			self.showWidget()
		elif reason == QSystemTrayIcon.DoubleClick:
			self.showWidget()
	
	@pyqtSlot()
	def showWidget(self):
		self.showNormal()
		self.raise_()
		self.activateWindow()
#		self.title_widget.turnPage(0)
	
	@pyqtSlot()	
	def showAboutUs(self):
		self.about_us_dialog.exec_()
	
	@pyqtSlot()	
	def showCharacter(self):
		self.character_widget.show()
	
	@pyqtSlot()	
	def showSettingDialog(self):
		self.setting_dialog.exec_()
	
	@pyqtSlot()	
	def changeSkin(self, skin_name): #QString 
		#Util.writeInit(QString("./user.ini"), QString("skin"), skin_name)
		self.skin_name = skin_name
		self.update()

	@pyqtSlot()	
	def changeQtab1(self):
		self.center_layout.removeWidget(self.content_widget)
		self.content_widget = Qtab1(self)
		self.center_layout.addWidget(self.content_widget)
	
	@pyqtSlot()	
	def changeQtab2(self):
		self.center_layout.removeWidget(self.content_widget)
		self.content_widget = Qtab2(self)
		self.center_layout.addWidget(self.content_widget)
	
	@pyqtSlot()	
	def changeQtab3(self):
		self.center_layout.removeWidget(self.content_widget)
		self.content_widget = Qtab3(self)
		self.center_layout.addWidget(self.content_widget)
	
	@pyqtSlot()	
	def changeQtab4(self):
		self.center_layout.removeWidget(self.content_widget)
		self.content_widget = Qtab4(self)
		self.center_layout.addWidget(self.content_widget)
	
	@pyqtSlot()	
	def changeQtab5(self):
		self.center_layout.removeWidget(self.content_widget)
		self.content_widget = Qtab5(self)
		self.center_layout.addWidget(self.content_widget)
	
	def isInTitle(self, xPos, yPos):
		return yPos < 300 and xPos < 695

class MyApplication(QApplication):
	
	def __init__(self, args):
		super(MyApplication, self).__init__(args)
	
	def GET_X_LPARAM(self, param):
		#define LOWORD(l)           ((WORD)((DWORD_PTR)(l) & 0xffff))
		#define HIWORD(l)           ((WORD)((DWORD_PTR)(l) >> 16))
		#define GET_X_LPARAM(lp)                        ((int)(short)LOWORD(lp))
		#define GET_Y_LPARAM(lp)                        ((int)(short)HIWORD(lp))
		return param & 0xffff

	def GET_Y_LPARAM(self, param):
		return param >> 16
	
	def winEventFilter(self, msg):
		if msg.message == 0x84: #WM_NCHITTEST
			form = self.activeWindow()
			if form:
				xPos = self.GET_X_LPARAM(msg.lParam) - form.frameGeometry().x()
				yPos = self.GET_Y_LPARAM(msg.lParam) - form.frameGeometry().y()
#				榧犳爣鍦ㄧ獥浣撹嚜瀹氫箟鏍囬鑼冨洿鍐咃紝绐椾綋鑷畾涔変竴涓猧sInTitle鐨勬柟娉曞垽鏂� 
#				if yPos < 30 and xPos < 456:
				if not form.isMaximized() and hasattr(form, 'isInTitle') and form.isInTitle(xPos, yPos):
					return True, 0x2 #HTCAPTION
			
		return False, 0

if __name__ == "__main__":

	import sys
	app = MyApplication(sys.argv)

	translator = QTranslator(app)
	translator.load(QString("qt_zh_CN.qm"))
	app.installTranslator(translator)
	
	translator_zh = QTranslator(app)
	translator_zh.load(QString("360safe_zh.qm"))
	app.installTranslator(translator_zh)
	app.setFont(QFont("Arial", 9))

	main_widget = MainWidget ()
	main_widget.showWidget()
	sys.exit(app.exec_())