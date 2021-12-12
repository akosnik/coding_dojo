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

    @classmethod
    def is_valid_name(cls, name):
        is_valid = True
        if len(name) < 2:
            flash("Names must be at least 2 characters.", "first_name")
            is_valid = False
        if len(name) > 45:
            flash("Names must be maximum 45 characters.", "first_name")
            is_valid = False
        return is_valid

    @classmethod
    def is_valid_email(cls, email):
        is_valid = True

        if not EMAIL_REGEX.match(email):
            print("6")
            flash("Invalid email address.", "email")
            is_valid = False
        return is_valid

    @classmethod
    def is_not_existing_email(cls, email):
        is_valid = True
        data = {
            'email': email
        }
        query = "SELECT email FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_schema').query_db(query, data)
        if len(results) > 0:
            flash("Email already exists.", "email")
            is_valid = False
        return is_valid

    @classmethod
    def is_valid_password(cls, password):
        is_valid = True

        if len(password) < 8 or len(password) > 32:
            flash("Password must be between 8 and 32 characters.", "password")
            is_valid = False

        if re.search("[a-z]", password) == None:
            flash("Password must contain at least one lowercase letter.", "password")
            is_valid = False

        if re.search("[A-Z]", password) == None:
            flash("Password must contain at least one uppercase letter.", "password")
            is_valid = False

        if re.search("[0-9]", password) == None:
            flash("Password must contain at least one number.", "password")
            is_valid = False

        if re.search("[!@#$%^&*()?._-]", password) == None:
            flash(
                "Password must contain at least one special character !@#$%^&*()?._-", "password")
            is_valid = False

        if PW_INVALIDS.match(password):
            flash("Only alphanumeric or !@#$%^&*()?._- characters allowed.", "password")
            is_valid = False

        return is_valid

    @classmethod
    def is_matching_password(cls, confirm, password):
        is_valid = True
        if password != confirm:
            flash("Passwords do not match.", "confirm")
            is_valid = False
        return is_valid

    @classmethod
    def is_valid_new_user(cls, user):
        is_valid = True
        if not(
            cls.is_valid_name(user['first_name'])
            and cls.is_valid_name(user['last_name'])
            and cls.is_valid_email(user['email'])
            and cls.is_not_existing_email(user['email'])
            and cls.is_valid_password(user['password'])
            and cls.is_matching_password(user['confirm_password'], user['password'])
        ):
            is_valid = False
        return is_valid

    @classmethod
    def login(cls, data):
        if not cls.is_valid_email(data['email']):
            flash("Invalid Email/Password", "login")
            return False
        if not cls.is_valid_password(data['password']):
            flash("Invalid Email/Password", "login")
            return False
        user = cls.get_user_by_email(data)
        if user == None:
            flash("Invalid Email/Password", "login")
            return False
        if not bcrypt.check_password_hash(user.password, data['password']):
            flash("Invalid Email/Password", "login")
            return False

        return user
