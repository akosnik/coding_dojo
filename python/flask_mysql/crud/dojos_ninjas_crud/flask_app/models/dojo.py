from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('db').query_db(query)

        dojos_list = []
        for item in results:
            dojos_list.append(cls(item))
        return dojos_list

    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('db').query_db(query, data)

        dojos = []
        for row in results:
            if len(dojos) == 0:
                new_dojo = cls(row)
                dojos.append(new_dojo)
            elif dojos[-1].id != row['id']:
                new_dojo = cls(row)
                dojos.append(new_dojo)

            if row['ninjas.id'] != None:
                new_ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'dojo_id': row['dojo_id'],

                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
                }
                new_ninja = Ninja(new_ninja_data)
                new_dojo.ninjas.append(new_ninja)
                new_ninja.dojo = new_dojo
        return dojos

    @ classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('db').query_db(query, data)

        dojos_list = []
        for item in results:
            dojos_list.append(cls(item))
        return dojos_list

    @ classmethod
    def create_new_dojo(cls, data):
        # the data comes from the html form.
        # connectToMySQL will unpack the data
        # the correct values get added into the query
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('db').query_db(query, data)
        return result
        # result is the primary key of the new dojo

    @ classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('db').query_db(query, data)
        return result

    @ classmethod
    def edit_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s"
        result = connectToMySQL('db').query_db(query, data)
        return result
