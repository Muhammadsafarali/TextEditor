# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(652, 531)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonClose = QtGui.QPushButton(self.centralwidget)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.buttonGroup = QtGui.QButtonGroup(notepad)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.buttonClose)
        self.gridLayout.addWidget(self.buttonClose, 0, 2, 1, 1)
        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.buttonGroup.addButton(self.buttonOpen)
        self.gridLayout.addWidget(self.buttonOpen, 0, 0, 1, 1)
        self.editorWindow = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorWindow.sizePolicy().hasHeightForWidth())
        self.editorWindow.setSizePolicy(sizePolicy)
        self.editorWindow.setObjectName(_fromUtf8("editorWindow"))
        self.gridLayout.addWidget(self.editorWindow, 2, 0, 1, 3)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout.addWidget(self.btnSave, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.buttonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "MainWindow", None))
        self.buttonClose.setText(_translate("notepad", "Close", None))
        self.buttonOpen.setText(_translate("notepad", "Open file", None))
        self.btnSave.setText(_translate("notepad", "Save", None))

