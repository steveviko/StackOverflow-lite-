from flask import Flask
from flask_restful import Resource, Api ,reqparse
from app.db import Users,questions,answers


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()



class Questions(Resource):
    #Fetch all questions
    def get(self):
        self.question = questions               
        return {'Questions':self.question},200
        

    #Add a question
    def post(self):
        parser.add_argument('question', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'question': '{} added successfully....'.format(args['question'])
        }

class Get_Single_question(Resource):
    #Fetch single questions
    def get(self, id):
        self.qn = questions
        Single_qn = [key for key in self.qn if key["id"] == id]
        if not Single_qn:
            return {'msg':'No available question for your search..!!!!'}

        return Single_qn,200
        

class Add_SingleQuestion(Resource):
    #Add  a question
    def put(self, id):
        parser.add_argument('question', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'question': 'The number  {} question was successfully submitted.'.format(id)
        },200

class Add_Answer(Resource):
    #Add an answer to a question
    def put(self, id):
        parser.add_argument('answer', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'answer': 'The answer number {} was successfully submitted.'.format(id)
        },200

api.add_resource(Questions, '/api/v1/questions/')
api.add_resource(Add_SingleQuestion, '/', '/api/v1/questions/<int:id>')
api.add_resource(Get_Single_question, '/', '/api/v1/questions/<int:id>')
api.add_resource(Add_Answer, '/', '/api/v1/questions/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)