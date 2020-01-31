



class PersonalDataCategory:

    def __init__(self, type_, purpose, legalBasis, dataController, processing, recipient):
        self.type_ = type_
        self.purpose = purpose
        self.legalBasis = legalBasis
        self.dataController = dataController
        self.processing = processing
        self.recipient = recipient



    def toString(self):

        data_string = "We use your " + self.type_
        data_string += " to " + ",".join(self.purpose)
        data_string += "\nOur legal basis to do this is " + ",".join(self.legalBasis)


        print(data_string)

