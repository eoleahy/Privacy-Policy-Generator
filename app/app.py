from flask import Flask, render_template, request 
#from personalDataCategory import PersonalDataCategory
import datetime
import rdflib
import json
import os
import sys


app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)
if(sys.platform=="win32"):
    json_path = os.path.join(BASE_PATH,"static\inputExample.json")
else:
    json_path = os.path.join(BASE_PATH,"static/inputExample.json")

@app.route('/', methods = ['GET'])

def policy():

    data = {}

    with open(json_path) as f:
        data = json.load(f)

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    purpose_set = set()

    for cat in data["personalDataCategory"]:
        purpose_set.update(cat["purpose"])

    data["date"] = date

    topics = ["What data do we collect?",
                "How will we collect your data?",
                "How will we use your data?",
                "How do we store your data?",
                "Who do we share your data with?",
                "Cookies",
                "What are your data protection rights?",
                "Changes to our privacy policy",
                "How to contact us"]

    return render_template('policy.html',
                            #dpv = g,
                            topics = topics,
                            data = data,
                            purpose_set=purpose_set
                            )



    '''
    g = rdflib.Graph()
    g.parse("static/dpv.ttl",format="ttl")

    for s,p,o in g:
        print(s)
    '''                            

if __name__ == '__main__':
    app.run()
    