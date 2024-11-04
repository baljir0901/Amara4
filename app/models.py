from app import db
from datetime import datetime

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Personal Information
    name_kanji = db.Column(db.String(100), nullable=False)
    name_furigana = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    
    # Contact Information
    current_address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    line_id = db.Column(db.String(100))
    
    # Education (stored as JSON)
    education = db.Column(db.JSON)
    
    # Work Experience (stored as JSON)
    work_experience = db.Column(db.JSON)
    
    # Qualifications
    japanese_license = db.Column(db.Boolean, default=False)
    mongolian_license = db.Column(db.Boolean, default=False)
    vietnamese_license = db.Column(db.Boolean, default=False)
    japanese_skill = db.Column(db.String(10))
    
    # Visa Information
    visa_status = db.Column(db.String(50))
    visa_expiry = db.Column(db.Date)
    
    # Health Information
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    blood_type = db.Column(db.String(5))
    allergies = db.Column(db.Boolean, default=False)
    allergy_details = db.Column(db.Text)
    smoking = db.Column(db.String(20))
    drinking = db.Column(db.String(20))
    
    # Emergency Contact
    emergency_contacts = db.Column(db.JSON)
    
    # File Paths
    photo_path = db.Column(db.String(200))
    resume_path = db.Column(db.String(200))
    id_card_path = db.Column(db.String(200))
    
    # Additional Information
    additional_info = db.Column(db.Text)

    def __repr__(self):
        return f'<Applicant {self.name_kanji}>'

class EmergencyContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    relationship = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))

    def __repr__(self):
        return f'<EmergencyContact {self.name}>'
