from flask import Flask, render_template, request, redirect, url_for, Markup
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Job, Application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talenthunt.db'  # Update to RDS later
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs')
def jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    job = Job.query.get_or_404(job_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.form['resume']
        application = Application(name=name, email=email, resume=resume, job_id=job.id)
        db.session.add(application)
        db.session.commit()
        return render_template('thanks.html', name=name)
    return render_template('apply.html', job=job)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            jobs = Job.query.all()
            applications = Application.query.all()
            return render_template('hr_dashboard.html', jobs=jobs, applications=applications)
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)

@app.route('/view_resume')
def view_resume():
    resume_content = request.args.get('resume_content', '')
    return f"""
    <html>
    <head><title>Resume</title></head>
    <body style='font-family:sans-serif;padding:20px'>
        <h2>Resume Preview</h2>
        <pre>{Markup(resume_content)}</pre>
        <a href="/login">Back to Dashboard</a>
    </body>
    </html>
    """

# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
