# backend holds the query info
from flask_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # this init, takes query info from a database as data
        # the right side is each column from the users table
        # this is how you turn your query result into python object

        def __repr__(self):
            return f"< first name: {self.first_name}, id:{self.id} > "

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        # The result from the query may be many entries (rows in my db)
        # We grab each entry (row) from results and turn them each into a User python object
        # then they're added to a list

        users_list = []
        for item in results:
            users_list.append(cls(item))
        return users_list

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query, data)

        users_list = []
        for item in results:
            users_list.append(cls(item))
        return users_list

    @classmethod
    def create_new_user(cls, data):
        # the data comes from the html form.
        # connectToMySQL will unpack the data
        # the correct values get added into the query
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
        # result is the primary key of the new user

    # Soon we will implement update and delete here
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        print("edit result", result)
        return result
