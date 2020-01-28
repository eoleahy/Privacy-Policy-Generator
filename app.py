from flask import Flask, render_template, request 
import datetime
import rdflib
import json

app = Flask(__name__)
json_path = "static/inputExample.json"

@app.route('/', methods = ['GET'])

def policy():

    data = {}

    with open(json_path) as f:
        data = json.load(f)

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    data["date"] = date

    topics = ["What data do we collect?",
                "How will we collect your data?",
                "How will we use your data?",
                "How do we store your data?",
                "Cookies",
                "What are your data protection rights?",
                "Changes to our privacy policy",
                "How to contact us"]

    return render_template('policy.html',
                            #dpv = g,
                            topics = topics,
                            data = data
                            )

def parse_rdf():

    '''
    g = rdflib.Graph()
    g.parse("static/dpv.ttl",format="ttl")

    for s,p,o in g:
        print(s)
    '''                            

if __name__ == '__main__':
    app.run()
    