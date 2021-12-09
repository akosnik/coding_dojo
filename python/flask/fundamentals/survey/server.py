from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'tbatstdgagitwamwtbatmro'


request_form = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/pass_info', methods=['POST'])
def pass_info():
    for key, val in request.form.items():
        session[key] = val

    return redirect('/result')


@app.errorhandler(404)
def not_found(e):
    return '404d! Must have taken a wrong turn at Albuquerque'


if __name__ == '__main__':
    app.run(debug=True)
