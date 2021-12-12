from flask_app import app, session
from flask import redirect, render_template, request
from flask_app.models.user import User
from flask_bcrypt import Bcrypt  # password encryption: pipenv install flask-bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    if 'user_id' not in session:
        session['user_id'] = False
        return redirect('/users/login')
    if session['user_id'] == False:
        return redirect('/users/login')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('show_user.html', user=user)


@app.route('/users/login')
def input_user():
    if session['user_id'] == False:
        return render_template('register_login_user.html')
    redirect(f'/users/show/{session["user_id"]}')


@app.post('/users/create')
def create_user():
    if not User.is_valid_new_user(request.form):
        return redirect(f'/users/login')

    # Does this go in model or controller?
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    result = User.insert_new_user(data)
    return redirect('/')


@app.post('/users/login')
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    session['user_id'] = User.login(data).id
    return redirect('/users/login')


@app.route('/users/logout')
def logout():
    session.clear()
    session['user_id'] = False
    return redirect('/')


# @app.route('/users/view')
# def view_users():
#     my_users = User.get_all_users()
#     return render_template('view_users.html', users=my_users)


@app.route('/users/show/<num>')
def show_user():
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('show_user.html', user=user)

# @app.route('/users/delete/<num>')
# def remove_user(num):
#     data = {
#         'id': num
#     }
#     User.delete_user(data)
#     return redirect('/users/view')


# @app.route('/users/edit/<num>')
# def edit_user(num):
#     data = {
#         'id': num
#     }
#     results = User.get_user(data)
#     return render_template('edit_user.html', user=results[0])


# @app.post('/users/edited/<num>')
# def edited_user(num):

#     if not User.is_valid_new_user(request.form):
#         return redirect(f'/users/edit/{num}')

#     data = {
#         'id': num,
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email']
#     }
#     User.edit_user(data)
#     return redirect(f'/users/show/{num}')
