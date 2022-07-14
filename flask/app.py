from flask import Flask, render_template, redirect, url_for
from forms import CandidatePersonalityForm
from BL.BusinessLayer import BusinessLayer
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'

businesslayer = BusinessLayer()

@app.route('/', methods=('GET', 'POST'))
def index():
    form = CandidatePersonalityForm()
    if form.validate_on_submit():

        businesslayer.addPersonalityTest(form)
        return redirect(url_for('roles'))
    return render_template('index.html', form=form)

@app.route('/roles/')
def roles():
    print("Roles entering")
    return render_template('roles.html',
                           personality_list=businesslayer.getPersonalityTest())

@app.route('/addroles/')
def add_roles():
    return render_template('addroles.html', personality_list=businesslayer.getPersonalityTest())

@app.route('/test')
def test_connection():
    return '<h1>test</h2>'

if __name__ == "__main__":
    app.run(debug=True)