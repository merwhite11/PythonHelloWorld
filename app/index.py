import json
import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'index_0.json')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():  # pragma: no cover
    Session = sessionmaker()

    # note sqlalchemy is modular so same logic for other DB types
    engine = create_engine("sqlite:///applications.db", echo=True)
    Session.configure(bind=engine)
    session = Session()
    return session



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