from flask import Flask, request, jsonify , render_template , redirect , Response , send_file
import requests
from function import *
from db import *
import datetime
dtime = datetime.datetime.now()
app = Flask(__name__)

response = {}
global dumtext
dumtext = {'Card':{
        'title': '`Title: this is a card title`',
        'text': 'This is the body text of a card.  You can even use line\n  breaks and emoji! 💁',
        'buttonText': 'Click me',
        'buttonUrl': 'https://assistant.google.com/'
    }}
global servayinfo
servayinfo = {
    'name': '',
    'email': '',
    'date': '',
    'socialmedia': '',
    'timeperiod': '',
    'priceing': ''
}
global loginstat
loginstat = False

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        password = str(request.form['typePasswordX-2'])
        personid = str(request.form['typeEmailX-2'])
        if password == '12345' and personid == 'admin':
            global loginstat
            loginstat = True
            return render_template('result.html',len = len(getall()),Pokemons =getall())

        else:
            return jsonify({'status':'Please Login'})

@app.route('/downloadcsv', methods=['GET'])
def downloadcsv():
    download_csv()
    if request.method=='GET':
        print('okkkkkk')
        if loginstat == True:
            return send_file('servaydata.csv', as_attachment=True)
                
        else:
            return jsonify({'status':'Please Login'})


@app.route('/api', methods=['GET', 'POST'])
def api():
    data = request.get_json()
    print(data)
   
    intent = data['queryResult']['intent']['displayName']
    if intent == 'currencyconverter':
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        
        cf = fetch_conversion_factor(source_currency,target_currency)
        final_amount = amount * cf
        final_amount = round(final_amount,2)
        response = {
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
        }
    elif intent == 'horoscope':
        print('-----------------------------------------------------')
        horiscopedates = str(data['queryResult']['parameters']['horiscopedates'])
        horiscopee = str(data['queryResult']['parameters']['horiscope'])
        result = horiscope(horiscopedates , horiscopee)
        response = {
            'fulfillmentText':f'Today horiscope for your sunsign {horiscopee} is {result}'
        }
    elif intent == 'Surveybot - yes-options - custom':
        print('-----------------------------------------------------')
        print(data['queryResult']['parameters']['person']['name'])
        servayinfo['name'] = str(data['queryResult']['parameters']['person']['name'])
        response = dumtext
    elif intent == 'Surveybot - yes-dates - custom - custom':
        print('-----------------------------------------------------')
        print(data)
        print(data['queryResult']['parameters']['socilamedia'])
        servayinfo['socialmedia'] = str(data['queryResult']['parameters']['socilamedia'])
        response = dumtext
    elif intent == 'Surveybot - yes- custom - price- custom':
        print('-----------------------------------------------------')
        print(data)
        print(data['queryResult']['queryText'])
        servayinfo['timeperiod'] = str(data['queryResult']['queryText'])
        response = dumtext
    elif intent == 'Surveybot - yes- custom - final- custom - custom':
        print('-----------------------------------------------------')
        print(data)
        print(data['queryResult']['queryText'])
        servayinfo['priceing'] = str(data['queryResult']['queryText'])
        response = dumtext
    elif intent == 'Surveybot - yes- custom - email':
        print('-----------------------------------------------------')
        print(data)
        print('-----------------------------------------------------')
        print(data['queryResult']['parameters']['email'])
        servayinfo['email'] = str(data['queryResult']['parameters']['email'])
        servayinfo['date'] = dtime
        update(data=servayinfo)
        print(getall())
        response = dumtext





    else:
        response = {
            'fulfillmentText':f"Sorry, I don't know how to {intent}"
        }
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)