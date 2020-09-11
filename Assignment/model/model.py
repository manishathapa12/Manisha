class Members:

    def __init__(self, ID, Name, Address, Gender, Contact, DOB, Email):
        self.ID=ID
        self.Name=Name
        self.Address=Address
        self.Gender=Gender
        self.Contact=Contact
        self.DOB = DOB
        self.Email = Email

    def set_ID(self,ID):
        self.ID= ID
    def get_ID(self):
        return self.ID

    def set_Name(self, Name):
        self.Name = Name
    def get_Name(self):
        return self.Name

    def set_Address(self, Address):
        self.Address = Address
    def get_Address(self):
        return self.Address

    def set_Gender(self,Gender):
        self.Gender = Gender
    def get_Gender(self):
        return self.Gender

    def set_Contact(self,Contact):
        self.Contact =Contact
    def get_Contact(self):
        return self.Contact

    def set_DOB(self, DOB):
        self.DOB = DOB
    def get_DOB(self):
        return self.DOB

    def set_Email(self,Email):
        self.Email = Email
    def get_Email(self):
        return self.Email



