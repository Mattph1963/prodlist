from flask import Flask
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/products')
def get_products():
    with open('products.json', 'r') as f:
        data = json.load(f)
    return data

@app.route('/getdealers/<product>')
def get_dealers(product):
    # Fetch dealers from dealerdetails
    dealer_url = "https://dealerdetails.onrender.com/allprice/" + product
    try:
        response = requests.get(dealer_url)
        data = response.json()
        if 'prices' in data:
            dealers = [price['key'] for price in data['prices']]
            return {'dealers': dealers}
        else:
            return {'dealers': []}
    except:
        return {'dealers': []}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)