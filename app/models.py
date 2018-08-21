from db import Users,questions,answers

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signup(self, user):
        Users.append(user)
        print("user successfully signed up")

    def login(self, username, password):
        for user in Users:
            if user.username == username and user.password == password:
                return True
        return False

    def logout(self):
        pass

    def post_question(self, question):        
        user_question = questions(question, self.username)
        questions.append(user_question)


class Questions:
    def __init__(self):
        self.question = {}


    def save_question(self, id , username, question):        
        id       =input("\n Enter an id number")
        username =input("\n Please Enter your username")
        question =input("\n Write a question %s:" % username)

        
        
    
