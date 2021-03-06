from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui
from NewContact import NewContForm
from ContactView import ContactViewForm
from ModelCM import Model

import sys
import qdarkstyle
import pickle

NAME, NUMBER, DATE, HIDDEN = range(4)

#The Widget where add a new contact
class NewContactForm(QtWidgets.QDialog, NewContForm):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setupUi(self)

#The Widget for the View of the contact
class ContactViewForm(QtWidgets.QDialog, ContactViewForm):
    def __init__(self,parent=None, name=None,surname=None,number=None,email=None,note=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setupUi(self, name,surname,number,email,note)        

#View Controller in MVC paradigm
class ViewController(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Contact Manager")
        MainWindow.resize(369, 629)

        #Database is implemented with the pickle module 
        #self.database = pickle.load( open( "save.p", "rb" ) )
        self.mod = Model(pickle.load( open( "save.p", "rb" )))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Model with 4 columns (NAME+SURNAME,NUMBER,EMAIL,HIDDEN). The hidden column is used for the filter
        self.model = QStandardItemModel(0, 4)
        self.model.setHeaderData(NAME, Qt.Horizontal, "Name")
        self.model.setHeaderData(NUMBER, Qt.Horizontal, "Number")
        self.model.setHeaderData(DATE, Qt.Horizontal, "Email")

        #The filter is created with the use of a QSortFilterProxyModel
        self.mProxyModelMenu = QSortFilterProxyModel()
        self.mProxyModelMenu.setDynamicSortFilter(True)
        self.mProxyModelMenu.setSourceModel(self.model)
        self.mProxyModelMenu.setFilterKeyColumn(3)

        #Call the method that initialize the contact list (eventually loading an existent list)
        self.generateList()

        #QTreeView for the view of ContactList
        self.tableWidget = QtWidgets.QTreeView(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 311, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRootIsDecorated(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setModel(self.mProxyModelMenu)
        self.tableWidget.setColumnHidden(3,True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #The event of doubleclick on Row
        self.tableWidget.doubleClicked.connect(self.editItem)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 311, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Line where search contact
        self.searchLineEdit = QtWidgets.QLineEdit(self.widget)
        self.searchLineEdit.setObjectName("searchlineEdit")
        #Connection of filtering model when press any key on searchLineEdit
        self.searchLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.horizontalLayout.addWidget(self.searchLineEdit)

        #The button for the Creation of a new Contact
        self.newContactButton = QtWidgets.QPushButton(self.centralwidget)
        self.newContactButton.setGeometry(QtCore.QRect(100, 560, 161, 51))
        self.newContactButton.setObjectName("newContactButton")
        self.newContactButton.clicked.connect(self.newContact)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def editItem(self):
        currentRow = self.tableWidget.currentIndex().row()
        text = self.tableWidget.selectedIndexes()[1].data(Qt.DisplayRole)
        
        #Call method to get index of correct element
        correctIndex = self.mod.getIndexContact(text)
        
        # Once it found the correct index of contact it open the contactView        
        cfv = ContactViewForm(None, self.mod.getElementName(correctIndex),self.mod.getElementSurname(correctIndex),self.mod.getElementNumber(correctIndex),
                                    self.mod.getElementEmail(correctIndex),self.mod.getElementNote(correctIndex))
        if cfv.exec_():
            # if True the user clicks delete element button else he saves the modifies in the database
            if cfv.deleteChoose: 
                self.mod.deleteContact(correctIndex)
            else:
                self.mod.editContact(correctIndex,cfv.name,cfv.surname,cfv.email,cfv.number,cfv.note)

            self.generateList()
             
    #this method set a filter for the SearchLineEdit
    def filterRegExpChanged(self):
        #The 0 value rappresents the choose of Regular Expression
        syntax = QRegExp.PatternSyntax(0)
        caseSensitivity = Qt.CaseSensitive
        regExp = QRegExp(self.searchLineEdit.text(),
                caseSensitivity, syntax)
        self.mProxyModelMenu.setFilterRegExp(regExp)

    #This method remove all rows and update with the element of database
    def generateList(self):
        self.model.removeRows( 0, self.model.rowCount() )
        for i in range(len(self.mod.database)):
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, NAME), self.mod.getElementName(i)+' '+self.mod.getElementSurname(i))
            self.model.setData(self.model.index(0, NUMBER), self.mod.getElementNumber(i))
            self.model.setData(self.model.index(0, DATE), self.mod.getElementEmail(i))
            self.model.setData(self.model.index(0, HIDDEN), self.mod.getElementEmail(i)+self.mod.getElementName(i)+
                               self.mod.getElementSurname(i)+self.mod.getElementNumber(i))
            
    #this method open a Widget where insert the contact values 
    def newContact(self):
        ncf = NewContactForm(None)
        if ncf.exec_():
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, NAME), ncf.name +' '+ ncf.surname)
            self.model.setData(self.model.index(0, NUMBER), ncf.number)
            self.model.setData(self.model.index(0, DATE), ncf.email)
            self.model.setData(self.model.index(0,HIDDEN), ncf.name +' '
                               + ncf.surname+' '+ str(ncf.number)+' '+ ncf.email)
            self.mod.addContact(ncf.name,ncf.surname,ncf.number,ncf.email,'')  
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Manager"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.newContactButton.setText(_translate("MainWindow", "New Contact"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = ViewController()
    ui.setupUi(window)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window.show()
    sys.exit(app.exec_())        