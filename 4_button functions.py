import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt tuts!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()
		
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(self.close_application)
		
		btn.resize(100,100)
		#btn.resize(btn.sizeHint())
		#btn.resize(btn.minimumSizeHint())
		
		btn.move(0,0)
		
		self.show()
		
	def close_application(self):
		print("whooaaaa so custom!!!")
		self.setWindowTitle("PyQt tuts!!!!!!")	
		
def run():		
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
run()