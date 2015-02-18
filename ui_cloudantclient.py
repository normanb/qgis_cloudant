# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cloudantclient.ui'
#
# Created: Thu Feb 12 11:08:43 2015
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_CloudantClient(object):
    def setupUi(self, CloudantClient):
        CloudantClient.setObjectName(_fromUtf8("CloudantClient"))
        CloudantClient.resize(524, 214)
        self.txtUrl = QtGui.QLineEdit(CloudantClient)
        self.txtUrl.setGeometry(QtCore.QRect(20, 30, 481, 20))
        self.txtUrl.setObjectName(_fromUtf8("txtUrl"))
        self.chkAuthentication = QtGui.QCheckBox(CloudantClient)
        self.chkAuthentication.setGeometry(QtCore.QRect(20, 60, 261, 17))
        self.chkAuthentication.setObjectName(_fromUtf8("chkAuthentication"))
        self.frmMain = QtGui.QFrame(CloudantClient)
        self.frmMain.setGeometry(QtCore.QRect(10, 90, 501, 111))
        self.frmMain.setAutoFillBackground(False)
        self.frmMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frmMain.setObjectName(_fromUtf8("frmMain"))
        self.cmdGetFeature = QtGui.QPushButton(self.frmMain)
        self.cmdGetFeature.setGeometry(QtCore.QRect(380, 80, 111, 23))
        self.cmdGetFeature.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cmdGetFeature.setObjectName(_fromUtf8("cmdGetFeature"))
        self.txtUsername = QtGui.QLineEdit(CloudantClient)
        self.txtUsername.setGeometry(QtCore.QRect(120, 110, 381, 20))
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.txtPassword = QtGui.QLineEdit(CloudantClient)
        self.txtPassword.setGeometry(QtCore.QRect(120, 140, 381, 20))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.lblUsername = QtGui.QLabel(CloudantClient)
        self.lblUsername.setGeometry(QtCore.QRect(20, 110, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName(_fromUtf8("lblUsername"))
        self.lblPassword = QtGui.QLabel(CloudantClient)
        self.lblPassword.setGeometry(QtCore.QRect(20, 140, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.cmdSaveUrl = QtGui.QPushButton(CloudantClient)
        self.cmdSaveUrl.setGeometry(QtCore.QRect(350, 60, 151, 23))
        self.cmdSaveUrl.setObjectName(_fromUtf8("cmdSaveUrl"))
        self.lblWarning = QtGui.QLabel(CloudantClient)
        self.lblWarning.setEnabled(False)
        self.lblWarning.setGeometry(QtCore.QRect(200, 10, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblWarning.setFont(font)
        self.lblWarning.setObjectName(_fromUtf8("lblWarning"))

        self.retranslateUi(CloudantClient)
        QtCore.QMetaObject.connectSlotsByName(CloudantClient)

    def retranslateUi(self, CloudantClient):
        CloudantClient.setWindowTitle(_translate("CloudantClient", "Client - Version 0.0.1", None))
        self.txtUrl.setText(_translate("CloudantClient", "https://cloudant.com/dbname", None))
        self.chkAuthentication.setText(_translate("CloudantClient", "Authentication required", None))
        self.cmdGetFeature.setText(_translate("CloudantClient", "GetFeature(s)", None))
        self.lblUsername.setText(_translate("CloudantClient", "Username", None))
        self.lblPassword.setText(_translate("CloudantClient", "Password", None))
        self.cmdSaveUrl.setText(_translate("CloudantClient", "Save URL as default", None))
        self.lblWarning.setText(_translate("CloudantClient", "<html><head/><body><p><span style=\" font-style:italic;\">Warning: Cloudant Error!</span></p></body></html>", None))

