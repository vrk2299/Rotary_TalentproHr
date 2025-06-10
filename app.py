from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Job, Application
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(minutes=30)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talenthunt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template("index.html", jobs=jobs)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template("job_detail.html", job=job)

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    email = request.form['email']
    resume_link = request.form['resume']
    job_id = request.form['job_id']
    new_app = Application(candidate_name=name, candidate_email=email, resume_link=resume_link, applied_job_id=job_id)
    db.session.add(new_app)
    db.session.commit()
    return render_template("apply_success.html", name=name)

@app.route('/hr/login', methods=['GET', 'POST'])
def hr_login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            session['user'] = user.username
            return redirect('/hr/dashboard')
        return "Invalid login"
    return render_template("hr_login.html")

@app.route('/hr/dashboard')
def hr_dashboard():
    if 'user' not in session:
        return redirect('/hr/login')
    apps = Application.query.all()
    return render_template("hr_dashboard.html", applications=apps)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
