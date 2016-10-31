#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from designer import Ui_notepad

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.buttonOpen, QtCore.SIGNAL("clicked()"), self.file_dialog)

    def file_dialog(self):
        self.ui.editorWindow.setText('aaaaaaaaaaaaaaaa')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())