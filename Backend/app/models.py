from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(255), nullable=False)
    contract_code = db.Column(db.Text, nullable=False)
