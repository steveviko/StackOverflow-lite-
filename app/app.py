from flask import Flask, render_template,url_for,request, jsonify
from models import Questions,Answers,questions

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello world"

@app.route('/api/v1/questions/', methods=['GET'])
def get_all_questions():
     return jsonify(questions)

@app.route('/api/v1/questions/<questionId>/', methods=['GET'])
def get_single_question(questionId):

    query = [key for key in questions if key["id"] == questionId]
    if query:
        return jsonify({'question': query}), 200
    else:
        return jsonify({"Error": "The question  is not available"}), 404

   
       
   
    
if __name__ == '__main__':
    app.run(debug=True)
