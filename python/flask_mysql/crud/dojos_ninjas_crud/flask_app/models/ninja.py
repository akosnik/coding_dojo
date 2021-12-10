from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"

        results = connectToMySQL('db').query_db(query)

        ninjas_list = []
        for item in results:
            ninjas_list.append(cls(item))
        return ninjas_list

    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL('db').query_db(query, data)

        ninjas_list = []
        for item in results:
            ninjas_list.append(cls(item))
        return ninjas_list

    @classmethod
    def create_new_ninja(cls, data):
        # the data comes from the html form.
        # connectToMySQL will unpack the data
        # the correct values get added into the query
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('db').query_db(query, data)
        return result
        # result is the primary key of the new ninja

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL('db').query_db(query, data)
        return result

    @classmethod
    def edit_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s"
        result = connectToMySQL('db').query_db(query, data)
        return result

    # select dropdown - set values to ids
