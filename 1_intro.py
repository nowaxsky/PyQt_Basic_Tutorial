import sys
from PyQt4 import QtGui
		
app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(30,30,500,300)
window.setWindowTitle("PyQt Tuts!")

window.show()