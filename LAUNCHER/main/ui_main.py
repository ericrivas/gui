# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setMinimumSize(QtCore.QSize(880, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(100, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
        self.stackedWidget.setStyleSheet("background-color: none;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_dashboard = QtWidgets.QWidget()
        self.page_dashboard.setObjectName("page_dashboard")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_dashboard)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_content_home = QtWidgets.QFrame(self.page_dashboard)
        self.frame_content_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_home.setObjectName("frame_content_home")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content_home)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_infos = QtWidgets.QFrame(self.frame_content_home)
        self.frame_infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_infos.setObjectName("frame_infos")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_infos)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_circle_1 = QtWidgets.QFrame(self.frame_infos)
        self.frame_circle_1.setMinimumSize(QtCore.QSize(215, 215))
        self.frame_circle_1.setMaximumSize(QtCore.QSize(215, 215))
        self.frame_circle_1.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(0, 170, 255);\n"
"    border-radius: 105px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(0, 170, 255, 150);\n"
"}\n"
"")
        self.frame_circle_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_1.setObjectName("frame_circle_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setContentsMargins(10, 50, 10, 50)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_circle_1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_circle_1)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_circle_1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
" color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_4.addWidget(self.frame_circle_1)
        self.frame_circle_2 = QtWidgets.QFrame(self.frame_infos)
        self.frame_circle_2.setMinimumSize(QtCore.QSize(215, 215))
        self.frame_circle_2.setMaximumSize(QtCore.QSize(215, 215))
        self.frame_circle_2.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(0, 170, 255);\n"
"    border-radius: 105px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(0, 170, 255, 150);\n"
"}")
        self.frame_circle_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_2.setObjectName("frame_circle_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_7.setContentsMargins(10, 50, 10, 50)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_circle_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_circle_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_circle_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: none;\n"
" color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.horizontalLayout_4.addWidget(self.frame_circle_2)
        self.frame_circle_3 = QtWidgets.QFrame(self.frame_infos)
        self.frame_circle_3.setMinimumSize(QtCore.QSize(215, 215))
        self.frame_circle_3.setMaximumSize(QtCore.QSize(215, 215))
        self.frame_circle_3.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(0, 170, 255);\n"
"    border-radius: 105px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(0, 170, 255, 150);\n"
"}")
        self.frame_circle_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_3.setObjectName("frame_circle_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_8.setContentsMargins(10, 50, 10, 50)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_circle_3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_circle_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_circle_3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: none;\n"
" color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.horizontalLayout_4.addWidget(self.frame_circle_3)
        self.verticalLayout_9.addWidget(self.frame_infos)
        self.verticalLayout_5.addWidget(self.frame_content_home)
        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_das = QtWidgets.QWidget()
        self.page_das.setObjectName("page_das")
        self.frame_content_credits = QtWidgets.QFrame(self.page_das)
        self.frame_content_credits.setGeometry(QtCore.QRect(90, 70, 120, 80))
        self.frame_content_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_credits.setObjectName("frame_content_credits")
        self.stackedWidget.addWidget(self.page_das)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(255, 255, 255, 150);")
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.frame_label_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits_bar)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "BH-X3 Dashboard"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "CURRENT ALTITUDE"))
        self.label_2.setText(_translate("MainWindow", "112"))
        self.label_3.setText(_translate("MainWindow", "ft"))
        self.label_5.setText(_translate("MainWindow", "SUPPLY DROP ALTITUDE"))
        self.label_6.setText(_translate("MainWindow", "89"))
        self.label_7.setText(_translate("MainWindow", "ft"))
        self.label_9.setText(_translate("MainWindow", "CDA DROP ALTITUDE"))
        self.label_10.setText(_translate("MainWindow", "127"))
        self.label_11.setText(_translate("MainWindow", "ft"))
        self.label_credits.setText(_translate("MainWindow", "2020-2021 UD ASAE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
