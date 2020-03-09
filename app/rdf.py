from rdflib import Graph, plugin, Namespace


class rdf():

    dpv_url = "http://w3.org/ns/dpv#"
    dpv = Namespace(dpv_url)

    @staticmethod
    def go():
        dpv_url = "http://w3.org/ns/dpv#"
        dpv = Namespace(dpv_url)
        print(dpv.hasProcessing)