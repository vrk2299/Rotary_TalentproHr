from app import db, User, Job

with db.app.app_context():
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
