from flask import Flask, render_template, request
from description import Description
from bs4 import BeautifulSoup
import datetime
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


    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    with open(json_path) as f:
        data = json.load(f)


    purpose_set = set()
    collect_set = set()
    
    data_classes = []

    #print(data)

    for cat in data["dpv:PersonalDataHandling"]:
        purpose_set.update(cat["dpv:hasPurpose"])
        collect_set.update(cat["dpv:Collect"])
        data_classes.append(cat["dpv:hasPersonalDataCategory"])

    collect_view = {}
    for collect in collect_set:
        collect_view[collect] = {}

    for key in collect_view:
        collect_view[key] = {"PersonalDataCategory":set(),
                             "Purpose":set(),
                             "Processing":set(),
                             "Recipient":set()}

        for cat in data["dpv:PersonalDataHandling"]:
            if(key in cat["dpv:Collect"]):
                collect_view[key]["PersonalDataCategory"].add(cat["dpv:hasPersonalDataCategory"])
                collect_view[key]["Purpose"].update(cat["dpv:hasPurpose"])
                collect_view[key]["Processing"].update(cat["dpv:hasProcessing"])
                collect_view[key]["Recipient"].update(cat["dpv:hasRecipient"])

    #print(collect_view)
    #print(data_classes)  
    dpvDescriptions = Description.descriptions(data_classes)
    #print(dpvDescriptions)
    data["date"] = date

    topics = [{"heading": "Personal Data View", "page": "data.html"},
              {"heading": "Collection View", "page": "collect.html"},
              {"heading": "Purpose View", "page": "purpose.html"},
              {"heading": "Data Storage View", "page": "store.html"},
              {"heading": "Data Sharing View", "page": "share.html"},
              {"heading": "Cookies", "page": "cookies.html"},
              {"heading": "Digital Rights View","page": "rights.html"},
              {"heading": "Changes to our privacy policy", "page": "changes.html"},
              {"heading": "How to contact us?", "page": "contact.html"}]

    return render_template('policy.html',
                           topics=topics,
                           data=data,
                           dpv=dpvDescriptions,
                           purpose_set=purpose_set,
                           collect=collect_view)


if __name__ == '__main__':
    app.run()
