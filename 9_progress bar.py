import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt tuts!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		
		extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		self.home()
		
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)
		
		extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'),'Flee the Scene', self)
		extractAction.triggered.connect(self.close_application)
		
		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)
		
		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100,25)
		checkBox.stateChanged.connect(self.enlarge_Window)
		
		### Add progress bar
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)
		
		### Maybe can just use btn2 = QtGui.Q...???
		self.btn = QtGui.QPushButton("Download",self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		###
		
		self.show()
	
	###	Add following lines
	def download(self):
		self.completed = 0
		
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)
	###	
		
	def enlarge_Window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(50,50,500,300)
		
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Extract!',
											"Get into the chopper?", 
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		
		if choice == QtGui.QMessageBox.Yes:
			print("Extracting Naaaaaaooooww!!!!")
			sys.exit()
		else:
			pass
	
		
def run():		
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
run()