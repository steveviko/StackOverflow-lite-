from flask import jsonify, request, json, make_response

questions =[]
class Questions():
    def __init__(self,title, text,answers,category):
        self.title = title
        self.text = text
        self.answers = []
        self.category = []


    def to_dict(self):
        result ={
                'id':len(questions) +1,
                'title':request.json['title'],
                'text':request.json['text']
                 }
        return result
    def get_answers(self):
        return self.answers


    def get_category(self):        
        return self.category 

class Answers():
    def __init__(self,qn_id,text):
        self.qn_id = qn_id
        self.text  = text

    def get_text(self):
            return self.text




    
        
        
    
