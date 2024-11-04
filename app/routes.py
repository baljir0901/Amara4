from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import SurveyForm
from app.models import Applicant

@app.route("/")
@app.route("/index")
def index():
    form = SurveyForm()
    return render_template("survey.html", title="Survey Form", form=form)

@app.route("/submit", methods=["POST"])
def submit():
    form = SurveyForm()
    if form.validate_on_submit():
        applicant = Applicant(
            name_kanji=form.name_kanji.data,
            name_furigana=form.name_furigana.data,
            birth_date=form.birth_date.data,
            gender=form.gender.data,
            nationality=form.nationality.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data
        )
        db.session.add(applicant)
        db.session.commit()
        flash("Application submitted successfully!")
        return redirect(url_for("thank_you"))
    return render_template("survey.html", title="Survey Form", form=form)

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html", title="Thank You")

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("500.html"), 500
