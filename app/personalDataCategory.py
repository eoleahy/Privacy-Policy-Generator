



class PersonalDataCategory:

    def __init__(self, type_, purpose, legal_basis, data_controller, processing, recipient):
        self.type_ = type_
        self.purpose = purpose
        self.legal_basis = legal_basis
        self.data_controller = data_controller
        self.processing = processing
        self.recipient = recipient



    def toString(self):

        data_string = "We use your " + self.type_
        data_string += " to " + ",".join(self.purpose)
        data_string += "\nOur legal basis to do this is " + ",".join(self.legal_basis)


        print(data_string)

