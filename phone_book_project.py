class PhoneBook:

    def __init__(self):
        self.list= []
      
    def add(self,contact):
        self.list.append(contact)

    def delete(self,name):
        print(self.list)
        for i in range( len(self.list)):
            contact = self.list[i] 
            if contact.name.upper().find(name.upper()) != -1:
                self.list.pop(i)
                break
            # else:
            #     print("No record found")
        print(self.list)
                 
    def search(self,name):
        for i in range(0,len(self.list),1):
            contact = self.list[i] 
            if contact.name.upper().find(name.upper()) != -1:
                print(contact)

            # if name.upper() == contact.name.upper():
            #     print(contact)


    #add, delete , list all contents, search



class Contact:
    
    def __init__(self,name,phone_no,emailid,areacode):
        self.name = name
        self.phone_no = phone_no
        self.emailid = emailid
        self.areacode = areacode 
        
    def __str__(self):
        return ",".join((self.name,self.phone_no,self.emailid,self.areacode))

    def __repr__(self):
        return ",".join((self.name,self.phone_no,self.emailid,self.areacode))
    

dave = Contact("Dave","12345","dave@gmail.com","011")
mike = Contact("Mike","4567","mike@gmail.com","099")
peter = Contact("Peter","89076","peter@gmail.com","897")
phonebook = PhoneBook()
phonebook.add(dave)
phonebook.add(mike)
phonebook.add(peter)
# phonebook.search("mi")
phonebook.delete("peter")

