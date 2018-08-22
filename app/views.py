import os
from flask import Flask, render_template,url_for,request, jsonify
from db import Users,questions,answers
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
#Fetch a single question 
def get_qn_id(id):
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

class Questions(Resource):
    def get(self):
        self.question = questions
        return self.question
     

    def post(self):
        parser.add_argument('question', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'question': '{} added...successfully'.format(args['question'])
        }
class SingleQuestion(Resource):
    def get(self):
        query = get_qn_id(id)
        if not query:
            return {'Response': 'question is not found'}, 404

        return query, 200





class Answers(Resource):
    def get(self):
        self.answer =answers
        return self.answer

    def put(self, id):
        parser.add_argument('answer', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'answer': 'The answer number {} was added...successfully'.format(id)
        }

api.add_resource(Questions, '/api/v1/questions/')
api.add_resource(SingleQuestion, '/api/v1/questions/<int:id>/')
if __name__ == '__main__':
    app.run(debug=True)