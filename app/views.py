from flask import Flask, render_template,url_for,request, jsonify
from app.db import Users,questions,answers

# Create some test data for our catalog in the form of a list of dictionaries.
users = [
    {'id': 0,
     'User FirstName': 'Moses',
     'User LasnName': 'Verno',
     'profession': 'Engineer.',
     'Age': '39'},
    {'id': 1,
     'User FirstName': 'Mike',
     'User LasnName': 'koola',
     'profession': 'Software Developer.',
     'Age': '16'},
    {'id': 2,
     'User FirstName': 'Chris',
     'User LasnName': 'looki',
     'profession': 'Doctor.',
     'Age': '12'},
]
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route('/api/v1/questions', methods=['GET'])
def api_all_questions():
    return jsonify(questions)
 

if __name__ == '__main__':
    app.run(debug=True)
