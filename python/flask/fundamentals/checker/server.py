from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', w=8, h=8, color1="black", color2="white")


@app.route('/<int:h>')
def height(h):
    return render_template('index.html', w=8, h=int(h), color1="black", color2="white")


@app.route('/<int:h>/<int:w>')
def height_width(h, w):
    return render_template('index.html', w=int(w), h=int(h), color1="black", color2="white")


@app.route('/<int:h>/<int:w>/<string:color1>/<string:color2>')
def colors(h, w, color1, color2):
    return render_template('index.html', w=int(w), h=int(h), color1=color1, color2=color2)


@app.errorhandler(404)
def not_found(e):
    return '404d! Must have taken a wrong turn at Albuquerque'


if __name__ == '__main__':
    app.run(debug=True)
