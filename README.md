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

## Getting Started

The project was developed with python3 . See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The libraries necessary for the use of the program are:

* PyQt5
* qdarkstyle
* pickle



### Step1: Improve Persistence
The first step was create ```Contact``` and ```ContactsBook``` classes and improve persistence for ```Contact``` class, this using the UsersDefault strategy, clearly explained in [this tutorial](https://developer.apple.com/documentation/foundation/userdefaults). Shortly, a file is created in the users folder (for me /Users/ME/Library/Containers/my-name.ContactManager/Data/Documents/contacts). This strategy obviusly isn't able to easly manage asynchronus changes: that's why i've not implemented this features.

```


