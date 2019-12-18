# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildrenForm2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(472, 334)
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 421, 301))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
