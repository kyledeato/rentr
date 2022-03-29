from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

class Rent: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM rents JOIN users ON rents.user_id = users.id;'
        results = connectToMySQL('rentr_db').query_db(query)
        rents = []
        if results:
            for row in results:
                temp_rents = cls(row)
                user_data = {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password": row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }
                temp_rents.creator = user.User(user_data)
                rents.append(temp_rents)
            return rents

    @classmethod
    def get_rents_by_id(cls, data):
        query = 'SELECT * FROM rents JOIN users ON rents.user_id = users.id WHERE users.id = %(id)s'
        results = connectToMySQL('rentr_db').query_db(query, data)
        rents = []
        if results:
            for row in results:
                temp_rents = cls(row)
                rents.append(temp_rents)
        return rents


    @classmethod
    def create(cls, data):
        query = 'INSERT INTO rents (name, description, location, user_id) VALUES (%(name)s, %(description)s, %(location)s, %(user_id)s)'
        return connectToMySQL('rentr_db').query_db(query, data)
    
    @staticmethod
    def is_valid(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if len(data['description']) < 10:
            flash("Description should be at least 10 characters long.")
            is_valid = False
        if len(data['location']) < 5:
            flash("Location should be at least 5 characters long.")
            is_valid = False
        return is_valid
