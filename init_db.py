from flask import Flask
from models import db, User, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talenthunt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add HR user
    admin = User(username="admin", password="password")
    db.session.add(admin)

    # Add sample jobs
    db.session.add(Job(title="SRE Engineer", description="Manage reliability of production systems."))
    db.session.add(Job(title="DevOps Engineer", description="CI/CD pipelines, infra as code, automation."))
    db.session.add(Job(title="Python Developer", description="Develop APIs and web apps using Python."))

    db.session.commit()
    print("Initialized DB with HR user and jobs.")
