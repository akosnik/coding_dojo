from flask import Flask, render_template
app = Flask(__name__)

users = [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'John', 'last_name': 'Supsupin'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


@app.route('/')
def index():
    return render_template('index.html', users=users)


@app.route('/<color>')
def color_table(color):
    return render_template('index.html', users=users, table_color=color)


@app.errorhandler(404)
def not_found(e):
    return '404d! Must have taken a wrong turn at Albuquerque'


if __name__ == '__main__':
    app.run(debug=True)
