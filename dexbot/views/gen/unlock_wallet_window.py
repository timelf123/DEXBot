# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dexbot/views/orig/unlock_wallet_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 141)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.helper_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helper_text.sizePolicy().hasHeightForWidth())
        self.helper_text.setSizePolicy(sizePolicy)
        self.helper_text.setAlignment(QtCore.Qt.AlignCenter)
        self.helper_text.setObjectName("helper_text")
        self.verticalLayout.addWidget(self.helper_text)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 126))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.form_wrap = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_wrap.sizePolicy().hasHeightForWidth())
        self.form_wrap.setSizePolicy(sizePolicy)
        self.form_wrap.setObjectName("form_wrap")
        self.formLayout = QtWidgets.QFormLayout(self.form_wrap)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.password_label = QtWidgets.QLabel(self.form_wrap)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_input = QtWidgets.QLineEdit(self.form_wrap)
        self.password_input.setMinimumSize(QtCore.QSize(200, 0))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.ok_button = QtWidgets.QPushButton(self.form_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_button.setObjectName("ok_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ok_button)
        self.horizontalLayout_3.addWidget(self.form_wrap)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.password_label.setBuddy(self.password_input)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unlock wallet"))
        self.helper_text.setText(_translate("Dialog", "Please enter your wallet password before continuing."))
        self.password_label.setText(_translate("Dialog", "Wallet password"))
        self.ok_button.setText(_translate("Dialog", "OK"))

