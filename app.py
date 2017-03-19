from flask import Flask, render_template, request, session, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from functools import wraps
from helpers import is_valid_login_password, get_user_details, get_all_tasks, update_new_task, create_user, \
    get_user_details_helper, mark_task_as_pending_helper, mark_task_as_complete_helper

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config.ProductionConfig')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


@app.route("/")
@login_required
def home():
    logged_in = "False"
    all_tasks = get_all_tasks(session['email'])
    pending_tasks = None
    completed_tasks = None
    if len(all_tasks['pending_tasks']) != 0:
        pending_tasks = all_tasks['pending_tasks']
    if len(all_tasks['completed_tasks']) != 0:
        completed_tasks = all_tasks['completed_tasks']
    if 'logged_in' in session:
        logged_in = 'True'
    return render_template('home.html', pending_tasks=pending_tasks, completed_tasks=completed_tasks,
                           logged_in=logged_in)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        user_details = get_user_details_helper(email)
        if 'password' in user_details and bcrypt.check_password_hash(user_details['password'], password):
            session['logged_in'] = True
            session['email'] = email
            return redirect(url_for('home'))
        else:
            flash("Email or Password provided are incorrect!!")
            return redirect(url_for('login'))
    return render_template('login.html')


# pending signup create new user
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'logged_in' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        re_password = request.form['password']
        if password != re_password:
            flash("Passwords do not match. Please try again!!")
        else:
            session['email'] = email
            session['logged_in'] = True
            create_user(email, bcrypt.generate_password_hash(password))
            return redirect(url_for('home'))
    return render_template('signup.html')


@app.route('/register')
def register():
    return redirect(url_for('signup'))


# return false if exists to stop proceeding
@app.route("/_check_email_signup", methods=['POST'])
def _check_email_signup():
    email = request.form["email"]
    if get_user_details(email) is None:
        return "true"
    else:
        return "false"


# if emails exists, return true.
# else return false and request to signup
@app.route("/_check_email_login", methods=['POST'])
def _check_email_login():
    email = request.form["email"]
    if get_user_details(email) is None:
        return "false"
    else:
        return "true"


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    flash('You were logged out.')
    return redirect(url_for('login'))


@app.route('/create_new_task', methods=['POST'])
@login_required
def create_new_task():
    update_new_task(request.form['new_task_title_value'], request.form['new_task_desription_value'],
                    session['email'])
    return 'true'


@app.route('/mark_task_complete', methods=['GET', 'POST'])
def mark_task_complete():
    task_id = request.form['task_id_toggle']
    mark_task_as_complete_helper(task_id, session['email'])
    return 'true'


@app.route('/mark_task_pending', methods=['GET', 'POST'])
def mark_task_pending():
    task_id = request.form['task_id_toggle']
    print 'task_id', task_id
    mark_task_as_pending_helper(task_id, session['email'])
    return 'true'


if __name__ == '__main__':
    app.run()
