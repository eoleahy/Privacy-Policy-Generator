class DPVClass:

    label = ""
    properties = []

    def __init__(self,iri):
        #print("Created ",type(self))
        self.iri=iri
        self.label = ""
        self.properties = []

class PersonalData(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)

class DataController(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)

    def generate_markup(self):

        markup = ""
 
        return markup    


class DataSubject(DPVClass):
    
    def __init__(self, iri):
        super().__init__(iri)

class Purpose(DPVClass):
  
    def __init__(self, iri):
        super().__init__(iri)

class Processing(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)

class LegalBasis(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)

class TechnicalOrgMeasure(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)

class Recipient(DPVClass):

    def __init__(self, iri):
        super().__init__(iri)
