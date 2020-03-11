

class PersonalDataHandling:

    iri = "" 
    properties = []

    def __init__(self,iri):
        self.iri = iri
        self.properties = []
        print("Created class:",self.iri)#
    

    def generate_markup(self,nodes):
        markup = ""



        for node in nodes:

            print(node,nodes[node])

        """
        markup =
        <div id=#{iri} resource=#{} typeof="dpv:{}">
        <h3>Your <span class="dpv:{}">{}</span>:</h3>
            {% include "dpvData.html" %}

        .format(iri=self.iri)    

        """
        return markup    