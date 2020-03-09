

class PersonalDataHandling:

    iri = "" 
    data_category = ""
    subject = ""
    controller = ""
    purpose = []
    processing = []
    recipient = []
    tech_org_measure = []
    legal_basis = ""

    def __init__(self,iri):
        self.iri = iri
        print("Created class:",self.iri)


    def generate_rdfa(self):
        markup = ""
        return markup    