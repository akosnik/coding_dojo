# mySQL connector: pipenv install pymysql
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt  # password encryption: pipenv install flask-bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_INVALIDS = re.compile(r'[^0-9a-zA-Z!@#$%^&*()?._-]')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # 'instance' method
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def insert_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('login_schema').query_db(query, data)
        return result
        # result is the primary key of the new row

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = (%(id)s)"
        results = connectToMySQL('login_schema').query_db(query, data)
        # If db is setup correctly, results should return an array with one result
        if len(results) < 1:
            return None
        result = cls(results[0])
        return result

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = (%(email)s)"
        results = connectToMySQL('login_schema').query_db(query, data)
        # If db is setup correctly, results should return an array with one result

        if len(results) < 1:
            return None
        result = cls(results[0])
        return result

    # @classmethod
    # def get_all_users(cls):
    #     query = "SELECT * FROM users;"

    #     results = connectToMySQL('login_schema').query_db(query)

    #     row_list = []
    #     for item in results:
    #         row_list.append(cls(item))
    #     return row_list

    # @classmethod
    # def update_user(cls, data):
    #     # The values are keys in the data dictionary. The keys should match up to the column names
    #     query = "UPDATE users SET (first_name, last_name, email, password) = (%(first_name)s, %(last_name)s, %(email)s, %(password)s) WHERE id = %(id)s"
    #     result = connectToMySQL('login_schema').query_db(query, data)
    #     return result

    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s"
    #     result = connectToMySQL('login_schema').query_db(query, data)
    #     return result

    @staticmethod
    def is_valid_first_name(name):
        is_valid = True
        if len(name) < 2:
            flash("Names must be at least 2 characters.", "first_name")
            is_valid = False
        if len(name) > 45:
            flash("Names must be maximum 45 characters.", "first_name")
            is_valid = False
        return is_valid

    @staticmethod
    def is_valid_last_name(name):
        is_valid = True
        if len(name) < 2:
            flash("Names must be at least 2 characters.", "last_name")
            is_valid = False
        if len(name) > 45:
            flash("Names must be maximum 45 characters.", "last_name")
            is_valid = False
        return is_valid

    @staticmethod
    def is_valid_email(email, login=False):
        if not EMAIL_REGEX.match(email):
            if not login:
                flash("Invalid email address.", "email")
            return False
        return True

    @staticmethod
    def is_not_existing_email(email, login=False):
        data = {
            'email': email
        }
        query = "SELECT email FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_schema').query_db(query, data)
        if len(results) > 0:
            if not login:
                flash("Email already exists.", "email")
            return False
        return True

    @staticmethod
    def is_valid_password(password, login=False):
        is_valid = True

        if len(password) < 8 or len(password) > 32:
            if not login:
                flash("Password must be between 8 and 32 characters.", "password")
            is_valid = False

        if re.search("[a-z]", password) == None:
            if not login:
                flash("Password must contain at least one lowercase letter.", "password")
            is_valid = False

        if re.search("[A-Z]", password) == None:
            if not login:
                flash("Password must contain at least one uppercase letter.", "password")
            is_valid = False

        if re.search("[0-9]", password) == None:
            if not login:
                flash("Password must contain at least one number.", "password")
            is_valid = False

        if re.search("[!@#$%^&*()?._-]", password) == None:
            if not login:
                flash(
                    "Password must contain at least one special character !@#$%^&*()?._-", "password")
            is_valid = False

        if PW_INVALIDS.match(password):
            if not login:
                flash(
                    "Only alphanumeric or !@#$%^&*()?._- characters allowed.", "password")
            is_valid = False

        return is_valid

    @staticmethod
    def is_matching_password(confirm, password):
        if password != confirm:
            flash("Passwords do not match.", "confirm")
            return False
        return True

    @staticmethod
    def is_valid_new_user(user):
        is_valid = True

        if not User.is_valid_first_name(user['first_name']):
            is_valid = False
        if not User.is_valid_last_name(user['last_name']):
            is_valid = False
        if not User.is_valid_email(user['email']):
            is_valid = False
        if not User.is_not_existing_email(user['email']):
            is_valid = False
        if not User.is_valid_password(user['password']):
            is_valid = False
        if not User.is_matching_password(user['confirm_password'], user['password']):
            is_valid = False

        return is_valid

    @staticmethod
    def login(data):
        if not User.is_valid_email(data['email'], login=True):
            flash("Invalid Email/Password", "login")
            return False
        if not User.is_valid_password(data['password'], login=True):
            flash("Invalid Email/Password", "login")
            return False
        user = User.get_user_by_email(data)
        if user == None:
            flash("Invalid Email/Password", "login")
            return False
        if not bcrypt.check_password_hash(user.password, data['password']):
            flash("Invalid Email/Password", "login")
            return False

        return user
