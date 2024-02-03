import json
import os
from flask import Flask, jsonify, request, render_template
# from flask_wtf.csrf import CSRFProtect
# from flask_pymongo import PyMongo
# from pymongo import MongoClient


app = Flask(__name__)
# app.config.update(
#     DEBUG=True,
#     SECRET_KEY="secret_sauce"
# )
# csrf = CSRFProtect()
# csrf.init_app(app)

# Configure MongoDB connection
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/bm25'
# mongo = PyMongo(app)

# client = MongoClient('mongodb://localhost:27017/bm25')
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'index_0.json')



@app.route('/')
def hello():
    return 'Hello, this is your Flask server!'

@app.route('/test', methods=['GET', 'POST'])
def make_request():
    try:
        if request.method == 'POST':
            print(request)
            data = request.form.get('data')
            return f"received data: {data}\n"
            # return render_template('display_data.html', data=data)
        else:
            with open(data_path, 'r') as json_file:
                data = json_file.read()
                return data
    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def post_data():
    response = requests.post(url, data=data)
    return response

if __name__ == "__main__":
    app.run(debug=True)