from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, SelectField, TextAreaField, 
                    FileField, BooleanField, IntegerField, RadioField)
from wtforms.validators import DataRequired, Email, Optional, Length, NumberRange

class SurveyForm(FlaskForm):
    # Language Selection
    language = SelectField('言語 / Language', choices=[
        ('ja', '日本語'), ('en', 'English'), 
        ('mn', 'Монгол'), ('vi', 'Tiếng Việt')
    ])

    # Personal Information
    name_kanji = StringField('氏名', validators=[DataRequired()])
    name_furigana = StringField('フリガナ', validators=[DataRequired()])
    birth_date = DateField('生年月日', validators=[DataRequired()])
    gender = SelectField('性別', choices=[
        ('male', '男性'), ('female', '女性'), ('other', 'その他')
    ], validators=[DataRequired()])
    nationality = StringField('国籍', validators=[DataRequired()])

    # Contact Information
    current_address = StringField('現住所', validators=[DataRequired()])
    phone = StringField('電話番号', validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    line_id = StringField('LINE ID', validators=[Optional()])

    # Education (Multiple entries)
    education_start = DateField('入学年月', validators=[Optional()])
    education_end = DateField('卒業年月', validators=[Optional()])
    school_name = StringField('学校名', validators=[Optional()])
    department = StringField('学部', validators=[Optional()])

    # Work Experience (Multiple entries)
    work_start = DateField('入社年月', validators=[Optional()])
    work_end = DateField('退社年月', validators=[Optional()])
    company_name = StringField('会社名', validators=[Optional()])
    job_description = TextAreaField('仕事内容、退社理由', validators=[Optional()])

    # Qualifications
    japanese_license = BooleanField('日本運転免許')
    mongolian_license = BooleanField('モンゴル運転免許')
    vietnamese_license = BooleanField('ベトナム運転免許')
    japanese_skill = SelectField('日本語能力', choices=[
        ('n1', 'N1'), ('n2', 'N2'), ('n3', 'N3'),
        ('n4', 'N4'), ('n5', 'N5'), ('none', 'なし')
    ])

    # Current Status
    visa_status = StringField('在留資格', validators=[Optional()])
    visa_expiry = DateField('在留期限', validators=[Optional()])

    # Health Information
    height = IntegerField('身長', validators=[Optional(), NumberRange(min=100, max=250)])
    weight = IntegerField('体重', validators=[Optional(), NumberRange(min=30, max=200)])
    blood_type = SelectField('血液型', choices=[
        ('a', 'A'), ('b', 'B'), ('o', 'O'), ('ab', 'AB')
    ], validators=[Optional()])
    
    allergies = BooleanField('アレルギー')
    allergy_details = TextAreaField('アレルギーの詳細', validators=[Optional()])
    
    smoking = RadioField('喫煙', choices=[
        ('no', 'いいえ'), ('yes', 'はい'), ('sometimes', '時々')
    ], validators=[Optional()])
    
    drinking = RadioField('飲酒', choices=[
        ('no', 'いいえ'), ('yes', 'はい'), ('sometimes', '時々')
    ], validators=[Optional()])

    # Emergency Contacts
    emergency_contact_name = StringField('緊急連絡先氏名', validators=[Optional()])
    emergency_contact_relation = StringField('続柄', validators=[Optional()])
    emergency_contact_phone = StringField('緊急連絡先電話番号', validators=[Optional()])
    emergency_contact_address = StringField('緊急連絡先住所', validators=[Optional()])

    # Document Upload
    photo = FileField('写真')
    resume = FileField('履歴書')
    id_card = FileField('身分証明書')

    # Additional Information
    additional_info = TextAreaField('備考', validators=[Optional()])
