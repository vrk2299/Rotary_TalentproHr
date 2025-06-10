from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)           # ✅ Add this
    email = db.Column(db.String(120), nullable=False)          # ✅ Add this
    resume = db.Column(db.Text, nullable=False)                # ✅ Add this
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))    # ✅ Add this

    job = db.relationship('Job', backref=db.backref('applications', lazy=True))
