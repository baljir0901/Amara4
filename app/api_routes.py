from flask import jsonify, request
from app import app, db
from app.models import Applicant
from app.api_config import limiter, API_PREFIX
from datetime import datetime

@app.route(f"{API_PREFIX}/submit", methods=["POST"])
@limiter.limit("100 per hour")
def api_submit():
    try:
        data = request.get_json()
        applicant = Applicant(
            name_kanji=data["name_kanji"],
            name_furigana=data["name_furigana"],
            birth_date=datetime.strptime(data["birth_date"], "%Y-%m-%d"),
            gender=data["gender"],
            nationality=data["nationality"]
        )
        db.session.add(applicant)
        db.session.commit()
        return jsonify({
            "status": "success",
            "application_id": applicant.id
        }), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route(f"{API_PREFIX}/applications", methods=["GET"])
@limiter.limit("1000 per hour")
def get_applications():
    applications = Applicant.query.all()
    return jsonify({
        "status": "success",
        "data": [{
            "id": app.id,
            "name": app.name_kanji,
            "created_at": app.created_at.isoformat()
        } for app in applications]
    })
