import pickle

class Model:
	def __init__(self, database):
		self.database = database

	def addContact(self,name,surname,email,number,note):
		self.database = pickle.load( open( "save.p", "rb" ) )
		self.database.append({'name': name,
								'surname': surname, 
								'email': email,
								'number': number,
								'note':''})
		pickle.dump( self.database, open( "save.p", "wb" ))
	def getIndexContact(self,text):
		i = -1
    	#the order of contacts in the table is different in the database, so the program search the contact
        #with the same number of contact clicked 
		for i in range(len(self.database)):
			if text == self.database[i]['number']:
				correctIndex = i
		return i
    
	def getElementName(self,i):
		return str(self.database[i]['name'])
	def getElementSurname(self,i):
		return str(self.database[i]['surname'])
	def getElementEmail(self,i):
		return str(self.database[i]['email'])
	def getElementNumber(self,i):
		return str(self.database[i]['number'])
	def getElementNote(self,i):
		return str(self.database[i]['note'])

	def deleteContact(self,i):
		self.database.pop(i)
    	#Load the changes of database in file.p
		pickle.dump( self.database, open( "save.p", "wb" ) )					            
    
	def editContact(self,i,name,surname,number,email,note):
		self.database[i] = {'name': name,
                            'surname': surname,
                            'email': email,
                            'number': number,
                            'note':note}
		pickle.dump( self.database, open( "save.p", "wb" ) )                                     
    		  
        