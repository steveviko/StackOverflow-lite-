from flask import Flask, render_template,url_for,request, jsonify
from app.db import Users,questions,answers


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"


#Fetch all questions
@app.route('/api/v1/questions/all', methods=['GET'])
def api_all_questions():
    return jsonify(questions)


#Fetch a specific question
@app.route('/api/v1/questions', methods=['GET'])
def api_question_id():
    # Check if an ID was provided in the URL.
    # If ID is provided, assign it to a var.
    # Else, display an error.
    if 'id' in request.args:        
        qn_id= int(request.args['id'])
    else:
        return "Error: No id  provided. Please specify an id."

    # Create an empty list for our array of results
    results = []

    # Loop through the data and match results that matches the requested ID.
    
    for question in questions:
        if question['id'] == qn_id:
            results.append(question)
        
    return jsonify(results)




 
if __name__ == '__main__':
    app.run(debug=True)
