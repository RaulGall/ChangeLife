from flask import Flask, render_template, redirect, url_for
from forms import CandidatePersonalityForm, RoleForm
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

@app.route('/addroles/',methods=('GET', 'POST'))
def add_roles():
    form = RoleForm()
    print("before submit")
    if form.validate_on_submit():
        print("enter")
        businesslayer.addRolePersonalityTest(form)
        return redirect(url_for('roles'))
    else:
        print({field.short_name: field.data for field in form
         if field.short_name != 'csrf_token'})
    return render_template('addroles.html', personality_list=businesslayer.getPersonalityTest(),
                           form=form)

@app.route('/test')
def test_connection():
    return '<h1>test</h2>'

@app.route('/questions/')
def questions():
    form = RoleForm()
    return render_template('questions.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)