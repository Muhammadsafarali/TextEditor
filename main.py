# -*- coding: utf-8 -*-
import codecs
import sys
from PyQt4 import QtCore, QtGui
from designer import Ui_notepad

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonOpen, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.btnSave, QtCore.SIGNAL("clicked()"), self.save)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            text = codecs.open(self.filename, "r", 'utf-8').read()
            self.ui.editorWindow.setText(text)

    def save(self):
        from os.path import isfile
        if isfile(self.filename):
            file = codecs.open(self.filename, "w", 'utf-8')
            file.write(unicode(self.ui.editorWindow.toPlainText()))
            file.close()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())