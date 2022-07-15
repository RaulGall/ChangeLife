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
        businesslayer.add_personality_test(form)

        return redirect(url_for('results', email=form.email.data))

    return render_template('index.html', form=form)


@app.route('/roles/')
def roles():
    return render_template('roles.html',
                           personality_list=businesslayer.get_roles_test())


@app.route('/addroles/', methods=('GET', 'POST'))
def add_roles():
    form = RoleForm()
    if form.validate_on_submit():
        businesslayer.add_role_test(form)
        return redirect(url_for('roles'))

    return render_template('addroles.html', personality_list=businesslayer.get_personality_test(),
                           form=form)


@app.route('/test')
def test_connection():
    return '<h1>test</h2>'


@app.route('/results/<email>')
def results(email):
    distances = businesslayer.get_calculate_distance(email)
    return render_template('results.html', distances=distances)


@app.route('/questions/')
def questions():
    form = RoleForm()
    return render_template('questions.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)