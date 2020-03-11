import datetime

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

        date = datetime.date.today()
        date = date.strftime("%B %d, %Y")

        markup = """
        <div class="section">
            <h1><span resource="#{iri}" typeof="dpv:DataController">{company}</span> Privacy Policy</h1>
            <p>Effective date:{date}</p>
            <p>This privacy policy will explain how our organization uses the personal data we collect from you when you use our website</p>
            <p>Some context to the phrasing used can be found <a href="http://w3.org/ns/dpv#">here</a>.</p>
        </div>
        """.format(iri=self.iri, company=self.label, date = date)
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
