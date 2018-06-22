from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class ContactViewForm(object):
    def setupUi(self, Form, name,surname,number,email,note):
        Form.setObjectName("Contact View")
        Form.resize(436, 333)
        self.form  = Form

        #Assign the values whith the contact values clicked
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email
        self.note=note
        #A boolean attribute to make decision Save/Delete
        self.deleteChoose  = False

        #Label is filled with icon of a profile
        self.iconLabel = QtWidgets.QLabel(Form)
        pixmap = QPixmap('img/profile.png')
        pixmap = pixmap.scaled(161, 161, transformMode=QtCore.Qt.SmoothTransformation)
        self.iconLabel.setPixmap(pixmap)
        self.iconLabel.setGeometry(QtCore.QRect(30, 10, 161, 161))
        self.iconLabel.setObjectName("label")
        
        #QLabel show the field where make annotation
        self.noteTextLabel = QtWidgets.QLabel(Form)
        self.noteTextLabel.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.noteTextLabel.setObjectName("noteTextLabel")
        
        #QTextEdit where insert some annotation about the contact
        self.noteTextEdit = QtWidgets.QTextEdit(Form)
        self.noteTextEdit.setGeometry(QtCore.QRect(103, 198, 311, 71))
        self.noteTextEdit.setObjectName("textEdit")
        #Initialize with the input value
        self.noteTextEdit.append(self.note)
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(210, 20, 211, 151))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        #Label show where is nameLineEdit 
        self.nameFieldLabel = QtWidgets.QLabel(self.widget)
        self.nameFieldLabel.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameFieldLabel)
        
        #LineEdit where user can modify name
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLineEdit.setText(self.name)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        
        #Label show where is surnameLineEdit 
        self.surnameFieldLabel = QtWidgets.QLabel(self.widget)
        self.surnameFieldLabel.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameFieldLabel)
        
        #LineEdit where user can modify surname
        self.surnameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.surnameLineEdit.setObjectName("lineEdit_2")
        self.surnameLineEdit.setText(self.surname)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameLineEdit)
        
        #Label show where is numberLineEdit 
        self.numberFieldLabel = QtWidgets.QLabel(self.widget)
        self.numberFieldLabel.setObjectName("numberFieldLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numberFieldLabel)
        
        #LineEdit where user can modify number
        self.numberLineEdit = QtWidgets.QLineEdit(self.widget)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.numberLineEdit.setText(self.number)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numberLineEdit)
        
        #Label show where is emailLineEdit 
        self.emailFieldLabel = QtWidgets.QLabel(self.widget)
        self.emailFieldLabel.setObjectName("emailFieldLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.emailFieldLabel)
        
        #LineEdit where user can modify email
        self.emailLineEdit = QtWidgets.QLineEdit(self.widget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.emailLineEdit.setText(self.email)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.emailLineEdit)

        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 290, 228, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Button for the event of save changes
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        
        #Button for the event of delete Contact
        self.deleteButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.deleteButton.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(Form)
        #The connection of method with the click events
        self.saveButton.clicked.connect(self.saveClick)
        self.deleteButton.clicked.connect(self.deleteClick)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    #This method sets True the deleteChoose attribute
    def deleteClick(self):
        self.deleteChoose  = True
        self.form.accept()
        
    #Method that saves current value of the QLineEdits
    def saveClick(self):
        self.name = self.nameLineEdit.text()
        self.surname = self.surnameLineEdit.text()
        self.number = self.numberLineEdit.text()
        self.email = self.emailLineEdit.text()
        self.note = self.noteTextEdit.toPlainText()
        self.form.accept()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ContactView"))
        self.noteTextLabel.setText(_translate("Form", "Add Notes"))
        self.nameFieldLabel.setText(_translate("Form", "Name"))
        self.surnameFieldLabel.setText(_translate("Form", "Surname"))
        self.numberFieldLabel.setText(_translate("Form", "Number"))
        self.emailFieldLabel.setText(_translate("Form", "Mail"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.deleteButton.setText(_translate("Form", "Delete"))

