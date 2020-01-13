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

    date = datetime.date.today()
    date = date.strftime("%B %d. %Y")

    topics = ["What data do we collect?",
                "How will we collect your data?",
                "How will we use your date?",
                "How do we store your data?",
                "Marketing",
                "What are your data protection rights?",
                "Add more topics...",
                "Changes to our privacy policy",
                "How to contact us",
                "How to contact the appropriate authorities?"]

    types_of_data =["Name","Email addresss","Phone number"]            

    return render_template('policy.html',
                            company=company_name,
                            date=date,
                            topic_list = topics,
                            types_of_data = types_of_data
                            )



if __name__ == '__main__':
    app.run()
