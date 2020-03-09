

class DataController:

    iri = ""
    name = ""
    address = ""
    email = "" 
    telephone = ""

    def __init__(self,iri):
        self.iri = iri
        print("Created Data Controller",self.iri)

    def get_iri(self):
        return self.iri

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def set_address(self,address):
        self.address=address
    
    def get_address(self):
        return self.address

    def set_email(self, email):
        self.email=email

    def get_email(self):
        return self.email
    
    def set_telephone(self,telephone):
        self.telephone=telephone

    def get_telephone(self):
        return self.telephone