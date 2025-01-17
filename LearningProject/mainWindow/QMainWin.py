import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.resize(400,200)
        self.status=self.statusBar()
        self.status.showMessage("Status bar show notification",5000)
        self.setWindowTitle("PYQT5 MainWindow samples")

if __name__ =="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())
