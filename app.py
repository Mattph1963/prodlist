from flask import Flask
from flask_cors import CORS
import json
import requests

from flask import Flask, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/products')
def get_products():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        if 'products' not in data or not isinstance(data['products'], list):
            return jsonify({"error": "Invalid products format"}), 500
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "products.json not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in products.json"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getdealers/<product>')
def get_dealers(product):
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