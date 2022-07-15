from flask import Flask, request, jsonify
import requests
from function import *
app = Flask(__name__)

response = {}



@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.get_json()
    print(data)
   
    intent = data['queryResult']['intent']['displayName']
    if intent == 'currencyconverter':
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']
        print('-----------------------------------------------------')
        print(f'this is the intent: {intent}')
        print(f'Source currency: {source_currency}')

        
        cf = fetch_conversion_factor(source_currency,target_currency)
        final_amount = amount * cf
        final_amount = round(final_amount,2)
        response = {
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
        }
    if intent == 'horoscope':
        print('-----------------------------------------------------')
        horiscopedates = str(data['queryResult']['parameters']['horiscopedates'])
        horiscopee = str(data['queryResult']['parameters']['horiscope'])
        result = horiscope(horiscopedates , horiscopee)
        response = {
            'fulfillmentText':f'Today horiscope for your sunsign {horiscopee} is {result}'
        }




    else:
        response = {
            'fulfillmentText':f"Sorry, I don't know how to {intent}"
        }
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)