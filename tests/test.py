from flask import Flask, request
from flask_restful import Resource, Api
import unittest
import json
from app.views import api, app,Questions,Add_Answer,Get_Single_question
from app.db import Users, questions, answers

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        

    def test_get_method_to_get_all_question(self):
         response = self.app.get('/api/v1/questions/',
                                content_type="application/json")
         self.assertEqual(response.status_code, 200)


    def test_get_method_to_get_single_question(self):
        response = self.app.get('/api/v1/questions/1',
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)


    def test_put_method_to_add_questions(self):
        response = self.app.put(
            '/api/v1/questions/1')       
        self.assertEqual(response.status_code, 200)
 
    def test_put_method_to_add_answer(self):
        response = self.app.put(
            '/api/v1/questions/1')       
        self.assertEqual(response.status_code, 200)
        

        
