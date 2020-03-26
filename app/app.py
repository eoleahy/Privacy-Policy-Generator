from flask import Flask, render_template, request
from description import Description
from view import View
from bs4 import BeautifulSoup
import datetime
import json
import re
import os
import sys


app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)

if(sys.platform == "win32"):
    json_path = os.path.join(BASE_PATH, "static\input.json")
else:
    json_path = os.path.join(BASE_PATH, "static/input.json")

@app.route('/', methods=['GET'])
def policy():

    data = {}

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    with open(json_path) as f:
        data = json.load(f)

    data["date"] = date

    collect_set = set()
    process_set = set()

    data_classes = []
    purposes= []
    
    #Creating sets of different data,purpose,collection and processing catagories
    for cat in data["dpv:PersonalDataHandling"]:
        collect_set.update(cat["dpv:Collect"])
        process_set.update(cat["dpv:hasProcessing"])
        data_classes.append(cat["dpv:hasPersonalDataCategory"])

    for purp in data["dpv:Purpose"]:
         purposes.append(purp["dpv:hasPurpose"]) 

    collect_view = View.create_collect_view(data,collect_set)

    #Assigning personal data categories to the relevant recipients 
    for recip in data["dpv:Recipient"]:
        recip["PersonalDataCategory"] = set()
        for cat in data["dpv:PersonalDataHandling"]:
            for cat_recip in cat["dpv:hasRecipient"]:
                if cat_recip == recip["resource"]:
                    recip["PersonalDataCategory"].add(cat["dpv:hasPersonalDataCategory"])

    dpvDescriptions = Description.descriptions(data_classes)
    dpvDescriptions.update(Description.descriptions(purposes))

    topics = [{"heading": "Personal Data View", "page": "Data-View.html"},
              {"heading": "Collection View", "page": "Collect-View.html"},
              {"heading": "Purpose View", "page": "Purpose-View.html"},
              {"heading": "Data Sharing View", "page": "Share-View.html"},
              {"heading": "Cookies", "page": "cookies.html"},
              {"heading": "Rights", "page": "Rights.html"}]

    return render_template('policy.html',
                           topics=topics,
                           data=data,
                           dpv=dpvDescriptions,
                           purposes=purposes,
                           collect=collect_view)


if __name__ == '__main__':
    app.run()
