# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pha2sen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(920, 383)
        self.translateButton = QtWidgets.QPushButton(Form)
        self.translateButton.setGeometry(QtCore.QRect(420, 190, 71, 23))
        self.translateButton.setObjectName("translateButton")
        self.inputText = QtWidgets.QTextEdit(Form)
        self.inputText.setGeometry(QtCore.QRect(40, 40, 351, 291))
        self.inputText.setObjectName("inputText")
        self.outputText = QtWidgets.QTextEdit(Form)
        self.outputText.setGeometry(QtCore.QRect(530, 40, 351, 291))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outputText.setFont(font)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.copyButton = QtWidgets.QPushButton(Form)
        self.copyButton.setGeometry(QtCore.QRect(410, 250, 91, 23))
        self.copyButton.setObjectName("copyButton")
        self.tips = QtWidgets.QLabel(Form)
        self.tips.setGeometry(QtCore.QRect(410, 300, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tips.sizePolicy().hasHeightForWidth())
        self.tips.setSizePolicy(sizePolicy)
        self.tips.setText("")
        self.tips.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tips.setWordWrap(True)
        self.tips.setObjectName("tips")

        self.retranslateUi(Form)
        self.translateButton.clicked.connect(self.on_translate)
        self.copyButton.clicked.connect(self.on_clipboard)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "去换行符工具"))
        self.translateButton.setText(_translate("Form", "转换 >>"))
        self.copyButton.setText(_translate("Form", "复制到剪贴板"))

    def on_translate(self):
        sen = ""
        pha = self.inputText.toPlainText().split('\n')
        if not (len(pha) == 1 and len(pha[0]) == 0):
            for line in pha:
                sen += line.strip() + " "
        sen = sen[:-1]
        self.outputText.setText(sen)
        self.tips.setText("")

    def on_clipboard(self):
        sentence = self.outputText.toPlainText()
        if len(sentence) == 0:
            self.tips.setText("错误：内容为空！")
        else:
            clipboard = QtGui.QGuiApplication.clipboard()
            clipboard.setText(sentence)
            self.tips.setText("已成功复制内容到剪贴板！")


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('icon.jpg'))
    widget.show()
    sys.exit(app.exec_())
