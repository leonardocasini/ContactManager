from PyQt5 import QtCore, QtGui, QtWidgets


class NewContForm(object):
    def setupUi(self, Form):
        Form.setObjectName("New Contact")
        Form.resize(283, 230)
        self.form = Form
        
        #Initialize attribute of contact
        self.name = None
        self.surname = None
        self.number = None
        self.email = None
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 10, 221, 131))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        #QLabel show the LineEdit where insert name
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        
        #An empty QLineEdit where the user insert the name of the new contact
        self.namelineEdit = QtWidgets.QLineEdit(self.widget)
        self.namelineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.namelineEdit)

        #QLabel show the LineEdit where insert surname
        self.surnameLabel = QtWidgets.QLabel(self.widget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)

        #An empty QLineEdit where the user insert the surname of the new contact
        self.surnameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.surnameLineEdit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameLineEdit)
        
        #QLabel show the LineEdit where insert number
        self.numberLabel = QtWidgets.QLabel(self.widget)
        self.numberLabel.setObjectName("numberLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.numberLabel)
        
        #An empty QLineEdit where the user insert the number of the new contact
        self.numberLineEdit = QtWidgets.QLineEdit(self.widget)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numberLineEdit)
        
        #QLabel show the LineEdit where insert email
        self.emailLabel = QtWidgets.QLabel(self.widget)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        
        #An empty QLineEdit where the user insert the email of the new contact
        self.emailLineEdit = QtWidgets.QLineEdit(self.widget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.emailLineEdit)
        
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 170, 228, 32))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #User creates a new Contact on click QPushButton 
        self.SaveButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.SaveButton.setObjectName("pushButton")
        #Connects the click of SaveButton with the saveClick method 
        self.SaveButton.clicked.connect(self.saveClick)
        self.horizontalLayout.addWidget(self.SaveButton)
        

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def saveClick(self):
        self.name = self.namelineEdit.text()
        self.surname = self.surnameLineEdit.text()
        self.number = self.numberLineEdit.text()
        self.email = self.emailLineEdit.text()
        self.form.accept()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Contact"))
        self.nameLabel.setText(_translate("Form", "Name"))
        self.surnameLabel.setText(_translate("Form", "Number"))
        self.numberLabel.setText(_translate("Form", "Email"))
        self.emailLabel.setText(_translate("Form", "Surname"))
        self.SaveButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Delete"))

