from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'tbatstdgagitwamwtbatmro'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():

    session['form'] = request.form
    return render_template('result.html', my_form=request.form)


@app.errorhandler(404)
def not_found(e):
    return '404d! Must have taken a wrong turn at Albuquerque'


if __name__ == '__main__':
    app.run(debug=True)
