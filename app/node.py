
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
        self.process = self.get_nodes_by_type("Process")
        self.purpose = self.get_nodes_by_type("Purpose")
        self.legal_basis = self.get_nodes_by_type("LegalBasis")
        self.recipient = self.get_nodes_by_type("Recipient")
        self.tech_org = self.get_nodes_by_type(
            "TechnicalOrganisationalMeasure")
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

        print("SELF{}", "IRI {} --- TYPE {} --- LABEL {}".format(type(self), self.iri,
                                                                 self.node_type, self.label))
        for prop in self.properties:
            print("---", prop)


class PDH(Node):

    def __init__(self, iri, node_type):
        super().__init__(iri, node_type)

    def print_self(self):
        return super().print_self()

    def assign_properties(self):

        self.data_subject = []
        self.data_controller = []
        self.purpose = []
        self.processing = []
        self.recipient = []
        self.legal_basis = []
        self.tech_org = []

        for prop in self.properties:

            if(prop[0] == "hasDataSubject"):
                self.data_subject.append(prop[1])

            elif(prop[0] == "hasPersonalDataCategory"):
                self.data_cat = prop[1]

            elif(prop[0] == "hasDataController"):
                self.data_controller.append(prop[1])

            elif(prop[0] == "hasPurpose"):
                self.purpose.append(prop[1])

            elif(prop[0] == "hasProcessing"):
                self.processing.append(prop[1])

            elif(prop[0] == "hasRecipient"):
                self.recipient.append(prop[1])

            elif(prop[0] == "hasTechnicalOrganisationalMeasure"):
                self.tech_org.append(prop[1])

            elif(prop[0] == "hasLegalBasis"):
                self.legal_basis.append(prop[1])

    def generate_markup(self):

        category = self.data_cat.label
        category_iri = self.data_cat.iri
        category_type = self.data_cat.node_type
        print(category)

        markup = """<div id="#DataView-{cat}" resource="#{cat_iri}" typeof="dpv:{cat_type}">""".format(cat=category,cat_iri=category_iri,cat_type=category_iri)
        markup += "<h2>Personal Data View</h2>"

        markup += "<h3>Your {}</h3>".format(category)

        if(len(self.purpose) > 0):

            markup += """
                <h4>Used for purposes:</h4>
                    <ul>
                    """
            for purp in self.purpose:
                markup += """
                 <li><span resource="#{self_iri}" typeof="dpv:PersonalDataHandling">
                    <span property="dpv:hasPersonalDataCategory" href="#{cat_iri}"></span>
                    <span property="dpv:hasPurpose" resource="#{iri}" typeof="dpv:Purpose">{label}</span>
                    </span></li>""".format(self_iri=self.iri, cat_iri=category_iri, iri=purp.iri,label=purp.label)
      
            markup += "</ul>"

        if(len(self.processing) > 0):

            markup += """
                <h4>Processing include:</h4>
                    <ul>
                    """
            for proc in self.processing:
                markup += """
                 <li><span resource="#{self_iri}" typeof="dpv:PersonalDataHandling">
                    <span property="dpv:hasPersonalDataCategory" href="#{cat_iri}"></span>
                    <span property="dpv:hasProcessing" resource="#{iri}" typeof="dpv:Processing">{label}</span>
                    </span></li>""".format(self_iri=self.iri, cat_iri=category_iri, iri=proc.iri,label=proc.label)
      
            markup += "</ul>"

        if(len(self.recipient) > 0):

            markup += """
                <h4>Shared with:</h4>
                <ul>
                    """
            for recip in self.recipient:
                markup += """
                 <li><span resource="#{self_iri}" typeof="dpv:PersonalDataHandling">
                    <span property="dpv:hasPersonalDataCategory" href="#{cat_iri}"></span>
                    <span property="dpv:hasRecipient" resource="#{iri}" typeof="dpv:Recipient">{label}</span>
                    </span></li>""".format(self_iri=self.iri, cat_iri=category_iri, iri=recip.iri,label=recip.label)
      
            markup += "</ul>"
       
        if(len(self.legal_basis) > 0):

            markup += """
                <h4>Our legal basis is :</h4>
                    <ul>
                    """
            for basis in self.legal_basis:
                markup += """
                 <li><span resource="#{self_iri}" typeof="dpv:PersonalDataHandling">
                    <span property="dpv:hasPersonalDataCategory" href="#{cat_iri}"></span>
                    <span property="dpv:hasLegalBasis" resource="#{iri}" typeof="dpv:LegalBasis">{label}</span>
                    </span></li>""".format(self_iri=self.iri, cat_iri=category_iri, iri=basis.iri,label=basis.label)
      
            markup += "</ul>"
        
        if(len(self.tech_org) > 0):

            markup += """
                <h4>The measures we take include:</h4>
                    <ul>
                    """
            for item in self.tech_org:
                markup += """
                 <li><span resource="#{self_iri}" typeof="dpv:PersonalDataHandling">
                    <span property="dpv:hasPersonalDataCategory" href="#{cat_iri}"></span>
                    <span property="dpv:hasTechnicalOrganisationalMeasure" resource="#{iri}" typeof="dpv:TechinicalOrganisationalMeasure">{label}</span>
                    </span></li>""".format(self_iri=self.iri, cat_iri=category_iri, iri=item.iri,label=item.label)
      
            markup += "</ul>"      
        
        markup +="</div>"
        
        #print(markup)
        return markup
