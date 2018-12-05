# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import banco
import admin

class Ui_Form(object):
    def setupUi(self, Form):
        self.tela = Form
        Form.setObjectName("Form")
        Form.resize(708, 418)
        Form.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.labelMatricula = QtWidgets.QLabel(Form)
        self.labelMatricula.setGeometry(QtCore.QRect(75, 126, 60, 31))
        self.labelMatricula.setObjectName("labelMatricula")
        self.labelCPF = QtWidgets.QLabel(Form)
        self.labelCPF.setGeometry(QtCore.QRect(99, 159, 30, 21))
        self.labelCPF.setObjectName("labelCPF")
        self.graphicsViewFoto = QtWidgets.QGraphicsView(Form)
        self.graphicsViewFoto.setGeometry(QtCore.QRect(490, 70, 171, 192))
        self.graphicsViewFoto.setObjectName("graphicsViewFoto")
        self.labelCampus = QtWidgets.QLabel(Form)
        self.labelCampus.setGeometry(QtCore.QRect(80, 220, 55, 21))
        self.labelCampus.setObjectName("labelCampus")
        self.lineEditNome = QtWidgets.QLineEdit(Form)
        self.lineEditNome.setGeometry(QtCore.QRect(140, 70, 301, 27))
        self.lineEditNome.setText("")
        self.lineEditNome.setObjectName("lineEditNome")
        self.lineEditSobrenome = QtWidgets.QLineEdit(Form)
        self.lineEditSobrenome.setGeometry(QtCore.QRect(140, 100, 301, 27))
        self.lineEditSobrenome.setText("")
        self.lineEditSobrenome.setObjectName("lineEditSobrenome")
        self.lineEditMatricula = QtWidgets.QLineEdit(Form)
        self.lineEditMatricula.setGeometry(QtCore.QRect(140, 130, 301, 27))
        self.lineEditMatricula.setText("")
        self.lineEditMatricula.setObjectName("lineEditMatricula")
        self.lineEditCPF = QtWidgets.QLineEdit(Form)
        self.lineEditCPF.setGeometry(QtCore.QRect(140, 160, 301, 27))
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.lineEditCurso = QtWidgets.QLineEdit(Form)
        self.lineEditCurso.setGeometry(QtCore.QRect(140, 190, 301, 27))
        self.lineEditCurso.setObjectName("lineEditCurso")
        self.lineEditCampus = QtWidgets.QLineEdit(Form)
        self.lineEditCampus.setGeometry(QtCore.QRect(140, 220, 301, 27))
        self.lineEditCampus.setObjectName("lineEditCampus")
        self.labelCurso = QtWidgets.QLabel(Form)
        self.labelCurso.setGeometry(QtCore.QRect(90, 190, 41, 21))
        self.labelCurso.setObjectName("labelCurso")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(92, 66, 45, 31))
        self.labelNome.setObjectName("labelNome")
        self.labelSobrenome = QtWidgets.QLabel(Form)
        self.labelSobrenome.setGeometry(QtCore.QRect(65, 96, 60, 31)) # pos X, Y tam Y , X
        self.labelSobrenome.setObjectName("labelSobrenome")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 51, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 241, 19))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)

        self.usuario = QtWidgets.QLineEdit(Form)
        self.usuario.setGeometry(QtCore.QRect(140, 250, 301, 27))
        self.usuario.setObjectName("senha")
        self.labelUsuario = QtWidgets.QLabel(Form)
        self.labelUsuario.setGeometry(QtCore.QRect(82, 253, 50, 16))
        self.labelUsuario.setObjectName("labelUsuario")

        self.senha = QtWidgets.QLineEdit(Form)
        self.senha.setGeometry(QtCore.QRect(140, 280, 301, 27))
        self.senha.setObjectName("senha")
        self.labelSenha = QtWidgets.QLabel(Form)
        self.labelSenha.setGeometry(QtCore.QRect(88, 283, 50, 16))
        self.labelSenha.setObjectName("labelSenha")

        self.confirmarSenha = QtWidgets.QLineEdit(Form)
        self.confirmarSenha.setGeometry(QtCore.QRect(140, 310, 301, 27))
        self.confirmarSenha.setObjectName("confirmarSenha")
        self.labelConfSenha = QtWidgets.QLabel(Form)
        self.labelConfSenha.setGeometry(QtCore.QRect(37, 313, 85, 16))
        self.labelConfSenha.setObjectName("labelConfSenha")

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText('1')
        self.lineEdit.setGeometry(QtCore.QRect(140, 340, 301, 25))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(71, 343, 60, 16))
        self.label.setObjectName("label")

        self.btnOk = QtWidgets.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(140, 380, 150, 27))
        self.btnOk.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(self.cadastrar)

        self.btnCancelar = QtWidgets.QPushButton(Form)
        self.btnCancelar.setGeometry(QtCore.QRect(291, 380, 150, 27))
        self.btnCancelar.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def cadastrar(self):
        temp = []
        temp.append(self.lineEditNome.text())
        temp.append(self.lineEditSobrenome.text())
        try:
            temp.append(int(self.lineEditMatricula.text()))
        except:
            print('E1')
            return
        temp.append(self.lineEditCPF.text())
        temp.append(self.lineEditCurso.text())
        temp.append(self.lineEditCampus.text())
        if self.senha.text() == self.confirmarSenha.text():
            temp.append(self.senha.text())
        else:
            print('Senha incorretas')
            return
        temp.append(self.usuario.text())
        try:
            temp.append(int(self.lineEdit.text()))
        except:
            print('E2')
            return
        banco.Banco().cadastrar(temp)
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = admin.Ui_Home()
        self.ui.setupUi(self.window)
        self.window.show()

    def cancelarCadastro(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = admin.Ui_Home()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro da Matrícula"))
        self.labelMatricula.setText(_translate("Form", "Matricula:"))
        self.labelCPF.setText(_translate("Form", "CPF:"))
        self.labelCampus.setText(_translate("Form", "Campus:"))
        self.labelCurso.setText(_translate("Form", "Curso:"))
        self.labelNome.setText(_translate("Form", "Nome:"))
        self.labelSobrenome.setText(_translate("Form", "Sobrenome:"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\"logo.png\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "Vinculação da Matrícula"))
        self.label.setText(_translate("Form", "ID Cartão:"))
        self.labelSenha.setText(_translate("Form", "Senha:"))
        self.labelUsuario.setText(_translate("Form", "Usuario:"))
        self.labelConfSenha.setText(_translate("Form", "Confirmar Senha:"))
        self.btnOk.setText(_translate("Form", "OK"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Solicitacao = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Solicitacao)
    Solicitacao.show()
    sys.exit(app.exec_())