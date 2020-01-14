from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def create_policy():

    company_name = ""

    if request.method == 'POST':
        company_name = request.form["company_name"]


    return render_template('create_policy.html')    

@app.route('/policy', methods = ['POST', 'GET'])
def policy():

    company_name = "Eoin"
    email = "eoin.97@live.ie"
    phone_number = "085 244 0001"
    address = "13 Waterloo Rd, Dublin 4, Dublin"

    date = datetime.date.today()
    date = date.strftime("%B %d. %Y")

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



if __name__ == '__main__':
    app.run()
