# controllers are middlemen handle routes
from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.user import User


@app.route('/users/view')
def view_users():
    # my_users is a list of python objects (converted from mysql query result)
    my_users = User.get_all_users()
    return render_template('view_users.html', users=my_users)


@app.route('/users/show/<num>')
def show_user(num):
    data = {
        'id': num
    }
    users_list = User.get_user(data)
    return render_template('show_user.html', user=users_list[0])


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
    result = User.create_new_user(data)
    return redirect(f'/users/show/{result}')


@app.route('/users/delete/<num>')
def remove_user(num):
    data = {
        'id': num
    }
    User.delete_user(data)
    return redirect('/users/view')


@app.route('/users/edit/<num>')
def edit_user(num):
    data = {
        'id': num
    }
    results = User.get_user(data)
    return render_template('edit_user.html', user=results[0])


@app.post('/users/edited/<num>')
def edited_user(num):
    data = {
        'id': num,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.edit_user(data)
    return redirect(f'/users/show/{num}')
