from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, Length

class SurveyForm(FlaskForm):
    name_kanji = StringField('氏名（漢字）/ Name (Kanji)', 
        validators=[DataRequired()])
    
    name_furigana = StringField('氏名（フリガナ）/ Name (Furigana)', 
        validators=[DataRequired()])
    
    birth_date = DateField('生年月日 / Date of Birth', 
        validators=[DataRequired()])
    
    gender = SelectField('性別 / Gender',
        choices=[
            ('male', '男性 / Male'),
            ('female', '女性 / Female'),
            ('other', 'その他 / Other')
        ],
        validators=[DataRequired()])
    
    nationality = StringField('国籍 / Nationality', 
        validators=[DataRequired()])
    
    email = StringField('メールアドレス / Email', 
        validators=[DataRequired(), Email()])
    
    phone = StringField('電話番号 / Phone Number', 
        validators=[DataRequired()])
    
    address = TextAreaField('住所 / Address', 
        validators=[DataRequired()])
    
    photo = FileField('写真 / Photo')
