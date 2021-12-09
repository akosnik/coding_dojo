# controllers are middlemen handle routes
from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.user import User


@app.route('/users/view')
def view_users():
    # my_users is a list of python objects (converted from mysql query result)
    my_users = User.get_all_users()
    return render_template('read_user.html', users=my_users)


@app.route('/users/new')
def input_user():
    return render_template('create_user.html')


@app.post('/users/create')
def create_user():
    print(request.form)

    # We turn the form information into a data dictionary for the server to deal with
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_new_user(data)
    return redirect('/users/view')
