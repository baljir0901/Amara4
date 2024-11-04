from app import db
from datetime import datetime

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_kanji = db.Column(db.String(100), nullable=False)
    name_furigana = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
