import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt tuts!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()
		
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		
		###
		btn.clicked.connect(self.close_application)
		
		btn.resize(100,100)
		
		#The sizeHint code will return what QT thinks is the best side for your button. 
		#btn.resize(btn.sizeHint())	
		
		#The minimumSizeHint will just return what QT thinks is the smallest reasonable size for your button.
		#btn.resize(btn.minimumSizeHint())
		
		###
		
		btn.move(0,0)
		
		self.show()
	
	### Add following lines	
	def close_application(self):
		print("whooaaaa so custom!!!")
		self.setWindowTitle("PyQt tuts!!!!!!")
	###
		
def run():		
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
run()