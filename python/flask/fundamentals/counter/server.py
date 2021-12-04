from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'tbatstdgagitwamwtbatmrobtjmstjtbtctcbtjbastfb'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    if request.form['count'] == 'Count':
        session['count'] += 1
    else:
        session['count'] += 2
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def session_zero():
    session['count'] = 0
    return redirect('/')


@app.errorhandler(404)
def not_found(e):
    return "404'd! Must have taken a wrong turn at Albuquerque."


if __name__ == '__main__':
    app.run(debug=True)
