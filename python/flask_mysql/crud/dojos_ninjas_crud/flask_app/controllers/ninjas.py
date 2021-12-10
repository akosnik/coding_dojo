from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas/new')
def new_ninja():
    dojo_list = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos=dojo_list)


@app.post('/ninjas/create')
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    result = Ninja.create_new_ninja(data)
    return redirect(f"/dojos/view/{request.form['dojo_id']}")
