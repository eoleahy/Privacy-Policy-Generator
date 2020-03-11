
class NodeGraph:

    def __init__(self, nodes):
        self.nodes = nodes

    def get_node_by_iri(self, iri):

        for node in self.nodes:
            if node.iri == iri:
                return node

        return None

    def get_nodes_by_type(self, node_type):

        nodes = [node for node in self.nodes if(node.node_type == node_type)]
        return nodes

    def assign_types(self):

        self.pdh = self.get_nodes_by_type("PersonalDataHandling")
        self.data_controller = self.get_nodes_by_type("DataController")[0]
        self.personal_data = self.get_nodes_by_type("PersonalDataCategory")
        self.process= self.get_nodes_by_type("Process")
        self.purpose= self.get_nodes_by_type("Purpose")
        self.legal_basis= self.get_nodes_by_type("LegalBasis")
        self.recipient = self.get_nodes_by_type("Recipient")
        self.tech_org = self.get_nodes_by_type("TechnicalOrganisationalMeasure")
        self.data_subject = self.get_nodes_by_type("DataSubject")

    def create_dc_markup(self, date):

        dc = self.data_controller
        markup = """
        <div class="section">
            <h1><span resource="#{iri}" typeof="dpv:DataController">{company}</span> Privacy Policy</h1>
            <p>Effective date:{date}</p>
            <p>This privacy policy will explain how our organization uses the personal data we collect from you when you use our website</p>
            <p>Some context to the phrasing used can be found <a href="http://w3.org/ns/dpv#">here</a>.</p>
        </div>
        """.format(iri=dc.iri, company=dc.label, date=date)
        return markup

    def create_pdh_markup(self):

        """
        markup = ""
        iri_dict = { "hasPersonalDataCategory" : [],
                    "hasDataController": [],
                    "hasRecipient": [],
                    "hasProcessing": [],
                    "hasDataSubject": [], 
                    "hasPurpose": [],
                    "hasTechnicalOrganisationalMeasure": [],
                    "hasLegalBasis": []}

        return markup
        """

        markup = ""

        return markup

    def print_graph(self):

        for node in self.nodes:
            node.print_self()

class Node:

    def __init__(self, iri, node_type):
        self.iri = iri
        self.node_type = node_type
        self.label = ""
        self.properties = []

    def print_self(self):

        print("IRI {} --- TYPE {} --- LABEL {}".format(self.iri,
                                                       self.node_type, self.label))
        for prop in self.properties:
            print("---", prop)

