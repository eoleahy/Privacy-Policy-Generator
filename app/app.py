from flask import Flask, render_template, request
#from personalDataCategory import PersonalDataCategory
import datetime
import rdflib
import json
import os
import sys


app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)
if(sys.platform == "win32"):
    json_path = os.path.join(BASE_PATH, "static\inputExample.json")
else:
    json_path = os.path.join(BASE_PATH, "static/inputExample.json")

views = ["dpv","dataSubject","dataController","thirdParty"]

@app.route('/', methods=['GET'])
def policy():

    data = {}
    

    with open(json_path) as f:
        data = json.load(f)

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    purpose_set = set()
    collect_set = set()

    for cat in data["personalDataCategory"]:
        purpose_set.update(cat["purpose"])
        collect_set.update(cat["collection"])

    data["date"] = date

    topics = [{"heading": "What data do we collect?", "page": "data.html"},
              {"heading": "How will we collect your data?", "page": "collect.html"},
              {"heading": "How will we use your data?", "page": "purpose.html"},
              {"heading": "How do we store your data?", "page": "store.html"},
              {"heading": "Who do we share your data with?", "page": "share.html"},
              {"heading": "Cookies", "page": "cookies.html"},
              {"heading": "What are your data protection rights?", "page": "rights.html"},
              {"heading": "Changes to our privacy policy", "page": "changes.html"},
              {"heading": "Data protection officer", "page": "dataprotection.html"},
              {"heading": "How to contact us?", "page": "contact.html"}]

    return render_template('policy.html',
                           #dpv = g,
                           topics=topics,
                           data=data,
                           purpose_set=purpose_set,
                           collect_set=collect_set)


if __name__ == '__main__':
    app.run()
