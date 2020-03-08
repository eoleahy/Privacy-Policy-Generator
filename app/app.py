from flask import Flask, render_template, request
from rdflib import Graph,plugin
from rdflib.serializer import Serializer
from bs4 import BeautifulSoup
import datetime
import requests
import rdflib
import json
import re
import os
import sys


app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)
if(sys.platform == "win32"):
    json_path = os.path.join(BASE_PATH, "static\inputExample.json")
else:
    json_path = os.path.join(BASE_PATH, "static/inputExample.json")



dpv_url = "http://w3.org/ns/dpv#"




@app.route('/', methods=['GET'])
def policy():

    data = {}

    with open(json_path) as f:
        data = json.load(f)

    #data = jsonld["@graph"]
    #print(data)

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    purpose_set = set()
    collect_set = set()

    data_classes = []

    for cat in data["personalDataHandling"]:
        purpose_set.update(cat["purpose"])
        collect_set.update(cat["collection"])
        data_classes.append(cat["category"])

    #print(data_classes)
    dpvDescriptions = descriptions(data_classes)
    #print(dpvDescriptions)
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
                           #dpv = g,
                           topics=topics,
                           data=data,
                           dpv=dpvDescriptions,
                           purpose_set=purpose_set,
                           collect_set=collect_set)


def descriptions(data):

    page = requests.get(dpv_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    descriptions = {x:get_description(soup,x.replace(" ", "-").lower()) for x in data}

    return descriptions


def get_description(soup, sectionId):

    div = soup.find("section", {"id": sectionId})
    return div

def read_rdf():
    return 1


if __name__ == '__main__':
    app.run()
