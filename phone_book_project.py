class PhoneBook:

    def __init__(self):
        self.list= {}
      
    def add(self,contact):
        self.list[contact.name] = contact
        print(contact)
    #add, delete , list all contents, search


class Contact:
    
    def __init__(self,name,phone_no,emailid,areacode):
        self.name = name
        self.phone_no = phone_no
        self.emailid = emailid
        self.areacode = areacode 
        
    def __str__(self):
        return ",".join((self.name,self.phone_no,self.emailid,self.areacode))


dave = Contact("Dave","12345","dave@gmail.com","011")
mike = Contact("Mike","4567","mike@gmail.com","099")

phonebook = PhoneBook()
phonebook.add(dave)
phonebook.add(mike)