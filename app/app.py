from flask import Flask, render_template, request
from rdflib import Graph, plugin, Namespace
from PersonalDataClasses import DataController, PersonalData, DataSubject, Purpose, Processing, Recipient, LegalBasis, TechnicalOrgMeasure
from personalDataHandling import PersonalDataHandling
from bs4 import BeautifulSoup
from node import Node, NodeGraph
import datetime
import requests
import rdflib
import json
import re
import os
import sys


app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)
file_path = os.path.join(BASE_PATH, "static\inputExample.ttl")

if(sys.platform == "win32"):
    json_path = os.path.join(BASE_PATH, "static\inputExample.json")
else:
    json_path = os.path.join(BASE_PATH, "static/inputExample.json")


views = ["default", "data", "purpose", "collection",
         "storage", "sharing", "legalBasis", "rights", "techOrgMeasures"]


dpv_classes = ["PersonalDataCategory", "DataController", "DataSubject", "Purpose",
               "Processing", "Recipient", "TechnicalOrganisationalMeasure", "LegalBasis"]
dpv_url = "http://w3.org/ns/dpv#"

class_map = {"PersonalDataCategory": PersonalData,
             "DataController": DataController,
             "DataSubject": DataSubject,
             "Purpose": Purpose,
             "Processing": Processing,
             "Recipient": Recipient,
             "LegalBasis": LegalBasis,
             "TechnicalOrganisationalMeasure": TechnicalOrgMeasure}

classes = []


@app.route('/', methods=['GET'])
def policy():

    data = {}

    trips = parse_rdf(file_path)
    g = parse_triples(trips)    

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    dc_markup = g.create_dc_markup(date)
    pdh_markup = g.create_pdh_markup()

    with open(json_path) as f:
        data = json.load(f)

    #data = jsonld["@graph"]
    # print(data)
    purpose_set = set()
    collect_set = set()

    data_classes = []

    for cat in data["personalDataHandling"]:
        purpose_set.update(cat["purpose"])
        collect_set.update(cat["collection"])
        data_classes.append(cat["category"])

    # print(data_classes)
    dpvDescriptions = descriptions(data_classes)
    data["date"] = date

    topics = [{"heading": "What data do we collect?", "page": "data.html"},
              {"heading": "How will we collect your data?", "page": "collect.html"},
              {"heading": "How will we use your data?", "page": "purpose.html"},
              {"heading": "How do we store your data?", "page": "store.html"},
              {"heading": "Who do we share your data with?", "page": "share.html"},
              {"heading": "Cookies", "page": "cookies.html"},
              {"heading": "What are your data protection rights?",
                  "page": "rights.html"},
              {"heading": "Changes to our privacy policy", "page": "changes.html"},
              {"heading": "Data protection officer",
                  "page": "dataprotection.html"},
              {"heading": "How to contact us?", "page": "contact.html"}]

    return render_template('policy.html',
                           topics=topics,
                           controller_markup = dc_markup,
                           data=data,
                           dpv=dpvDescriptions,
                           purpose_set=purpose_set,
                           collect_set=collect_set)


def descriptions(data):

    page = requests.get(dpv_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    descriptions = {x: get_description(
        soup, x.replace(" ", "-").lower()) for x in data}

    return descriptions


def get_description(soup, sectionId):

    div = soup.find("section", {"id": sectionId})
    return div


def parse_rdf(file_path):

    g = Graph()
    g.parse(file_path, format="ttl")

    triples = []
    # Cleaning the triples
    for s, p, o in g:

        sub = (s.split('#')[1])

        pred = ""
        if("#") in p:
            pred = (p.split('#')[1])
        else:
            pred = str(p)

        obj = ""

        if(type(o) == rdflib.term.Literal):
            #print("literal found:",o)
            obj = (str(o))
        elif(type(o) == rdflib.term.URIRef):
            if("#" in o):
                obj = (o.split('#')[1])

        triples.append((sub, pred, obj))

    # TODO create class for purposes etc, load into dict by IRI, load into corresponding classes
    # print(triples)
    return triples


def parse_triples(triples):

    # Creating the base instances
    nodes = {}
    pdh = {}
    preds_filter = ["type", "label"]
    pdh_properties = ["hasRecipient", "hasPersonalDataCategory",
                      "hasDataController", "hasDataSubject"]
    dc_iri = ""



    node_declare = [x for x in triples if (x[1] == "type")]
    labels = [x for x in triples if(x[1] == "label")]
    dc_properties = [x for x in triples if ("schema.org" in x[1])]
    # Filtering the predicates
    triples = [x for x in triples if (x[1] not in preds_filter)]
    

    nodes = [Node(x[0],x[2]) for x in node_declare]

    g = NodeGraph(nodes)

    for s,p,o in labels:
        node = g.get_node_by_iri(s)
        node.label = o

    #Assign purpose,process. etc to the graph
    g.assign_types()
    #Find the properties for each node in the graph
    for s,p,o in triples:

        #print(s,p,o)
        node = g.get_node_by_iri(s)
        node.properties.append((p,g.get_node_by_iri(o)))
   
    g.print_graph()
    return (g) #Return the graph


if __name__ == '__main__':
    app.run()
