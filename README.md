# Contact Manager

A simple project for the exam of Human Computer Interaction.The Contact Manager implements below properties:
- [x] Visualization of all contacts
- [x] Allow to order contacts by each fiel displayed
- [x] Single contact visualization
- [x] Insertion of a new one
- [x] Contact persistence
- [x] Contact tagging and tag search
- [x] Contact editing
- [x] Full text search
```MainWindow``` consists of a list of contacts and a line where user can search contact. With a button user open ```NewContForm``` where create a new contact.       

![CM](https://github.com/leonardocasini/ContactManager/blob/master/Mockup/mockup.png)

### Prerequisites

The libraries necessary for the use of the program are:

* PyQt5
* qdarkstyle
* pickle



### Step1: Improve Persistence
The persistance of contacts was obtained through the module pickle. Contact is an object consisting of four attributes:
 * name
 * surname
 * email
 * notes: field text where make some annotation.

This module create a database save.p where the user can store an array of contact. 

```


