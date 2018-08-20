from app.db import users,questions,answers
import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signup(self, user):
        users.append(user)
        print("user signed up")

    def login(self, username, password):
        for user in users:
            if user.username == username and user.password == password:
                return True
        return False

    def logout(self):
        pass

    def post_question(self, question):
        timestamp = datetime.datetime.now()
        user_question = Question(question, self.username, timestamp)
        questions.append(user_question)


		
class Questions:    
    def __init__(self):
        self.question= {}
	


class Answers:
    def __init__(self):
        self.answer = {}





