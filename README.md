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



### Prerequisites

The libraries necessary for the use of the program are:

* PyQt5
* qdarkstyle
* pickle



### Step1: Improve Persistence
The persistance of contacts was obtained through the module pickle. This module create a databasse save.p where the user can store the contact. ContactList is made by an array of element consisting of four attributes [name,surname,email,notes].

```


