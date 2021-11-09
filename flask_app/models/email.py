from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,redirect,request
from flask_app.controllers import emails
import re



class Register:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def validate_email(email_data):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL('email_schemas').query_db(query,email_data)
        if len(results) >= 1:
            flash("email already taken")
            return False
        if not email_reg.match(email_data["email"]):
            flash("Invalid Email")
            is_valid = False
        flash("Valid Email")
        return is_valid

    @classmethod
    def saveemail(cls,data):
                query="INSERT into emails (email) VALUES(%(email)s)"
                return connectToMySQL("email_schemas").query_db(query,data)

    @classmethod
    def get_email(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('email_schemas').query_db(query)
        email_data = []

        for e in results: 
            email_data.append(cls(e))
        return email_data