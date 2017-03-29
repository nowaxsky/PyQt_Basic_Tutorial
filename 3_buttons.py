import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt tuts!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		###
		self.home()
		###
	
	### Add button	
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		btn.resize(100,100)
		btn.move(100,100)
		
		self.show()
	###

### Add following lines	
# or use def main()		
def run():		
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
run()
###