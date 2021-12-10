from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/dojos/view')
def view_dojos():
    my_dojos = Dojo.get_all_dojos()
    return render_template('view_dojos.html', dojos=my_dojos)


@app.route('/dojos/view/<d_id>')
def show_dojo(d_id):
    data = {
        'id': d_id
    }
    dojo = Dojo.get_ninjas_from_dojo(data)
    return render_template('show_dojo.html', dojo=dojo[0])


@app.post('/dojos/create')
def create_dojo():
    data = {
        'name': request.form['name']
    }
    d_id = Dojo.create_new_dojo(data)
    return redirect('/dojos/view')
