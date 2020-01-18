from flask import Flask, render_template, request 
from wtforms import Form, BooleanField, StringField, validators
from flask_bootstrap import Bootstrap
import datetime
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def create_policy():

    args={}
    #args["is_website"] = False
    #args["is_app"] = False

    if request.method == 'POST':
        args["company_name"] = request.form["company_name"]
        args["website_url"] = request.form["web_url"]
        args["email_addr"] = request.form["email_addr"]
        args["tel_number"] = request.form["tel_number"]
        args["street_addr"] = request.form["street_addr"]
        args["zip"] = request.form["zip"]
        args["country"] = request.form["country"]

        #print(request.form["is_website"])
        args["is_website"] = request.form.get("is_website") != None
        args["is_app"] = request.form.get("is_app") != None
        args["collects_email"] = request.form.get("collects_email") != None
        args["collects_name"] = request.form.get("collects_name") != None
        args["collects_phone"] = request.form.get("collects_phone") != None
        args["collects_address"] = request.form.get("collects_address") != None
        args["collects_smi"] = request.form.get("collects_smi") != None
        args["collects_others"] = request.form.get("collects_others") != None

        args["has_cookies"] = request.form.get("has_cookies") != None
        args["has_advertisements"] = request.form.get("has_advertisements") != None
        args["has_tracking"] = request.form.get("has_tacking") != None
        args["has_payments"] = request.form.get("has_payments") != None
        args["external_links"] = request.form.get("external_links") != None
        args["collects_u18"] = request.form.get("collects_u18") != None
        args["collects_u13"] = request.form.get("collects_u13") != None
    

    return render_template('create_policy.html',
                            page_vars=args)    

@app.route('/policy', methods = ['POST', 'GET'])
def policy():

    company_name = "Testcompany"
    email = "test@test.ie"
    phone_number = "12345678"
    address = "13 Waterloo Rd, Dublin 4, Dublin"

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    topics = ["What data do we collect?",
                "How will we collect your data?",
                "How will we use your data?",
                "How do we store your data?",
                "Marketing",
                "What are your data protection rights?",
                "Add more topics...",
                "Changes to our privacy policy",
                "How to contact us",
                "How to contact the appropriate authorities?"]

    types_of_data = ["Name",
                    "Email addresss",
                    "Phone number",
                    "etc"]        

    collection_types = ["Register online.",
                        "Place an order for any of our products or services.",
                        "Voluntarily complete a customer survey or provide feedback on any of our message boards or via email.",
                        "Use or view our website via your browser's cookies.",
                        "[Add extra]"]    

    data_usage = ["Manage your account.",
                  "Process your order.",
                  "Email you with special offers on other products and services we think you might like.",
                  "etc"]

    data_sharing_recip = ["Amazon.co.uk",
                         "etc"]

    contact_methods = ["Email us at: " + email,
                       "Call us: " + phone_number,
                       "Or write to us at: " + address]                 

    return render_template('policy.html',
                            company=company_name,
                            date=date,
                            topic_list = topics,
                            types_of_data = types_of_data,
                            collection_types = collection_types,
                            data_usage = data_usage,
                            data_sharing = data_sharing_recip,
                            contact_methods = contact_methods
                            )

Bootstrap(app)


if __name__ == '__main__':
    app.run()
