from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import app, db
from app.models import Applicant, User
from app.api_config import limiter, cache, API_PREFIX, ERROR_MESSAGES
from datetime import datetime
import hashlib

# Authentication endpoints
@app.route(f"{API_PREFIX}/auth/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()
        
        if user and user.check_password(data.get('password')):
            access_token = create_access_token(identity=user.email)
            return jsonify({
                'status': 'success',
                'access_token': access_token
            }), 200
        
        return jsonify({
            'status': 'error',
            'message': 'Invalid credentials'
        }), 401
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Protected API endpoints
@app.route(f"{API_PREFIX}/submit", methods=["POST"])
@jwt_required()
@limiter.limit("100 per hour")
def api_submit():
    try:
        data = request.get_json()
        current_user = get_jwt_identity()
        
        # Create new applicant
        applicant = Applicant(
            name_kanji=data["personal_info"]["name_kanji"],
            name_furigana=data["personal_info"]["name_furigana"],
            birth_date=datetime.strptime(data["personal_info"]["birth_date"], "%Y-%m-%d"),
            gender=data["personal_info"]["gender"],
            nationality=data["personal_info"]["nationality"],
            submitted_by=current_user
        )
        
        db.session.add(applicant)
        db.session.commit()
        
        # Clear cache for this user's applications
        cache.delete(f'applications_{current_user}')
        
        return jsonify({
            "status": "success",
            "message": "Application submitted successfully",
            "application_id": applicant.id
        }), 201
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route(f"{API_PREFIX}/application/<int:id>", methods=["GET"])
@jwt_required()
@limiter.limit("1000 per hour")
@cache.memoize(300)  # Cache for 5 minutes
def get_application(id):
    try:
        current_user = get_jwt_identity()
        cache_key = f'application_{id}_{current_user}'
        
        # Try to get from cache
        cached_result = cache.get(cache_key)
        if cached_result:
            return jsonify(cached_result)
        
        applicant = Applicant.query.get(id)
        if not applicant:
            return jsonify({
                "status": "error",
                "message": "Application not found"
            }), 404
            
        # Check if user has access to this application
        if applicant.submitted_by != current_user:
            return jsonify({
                "status": "error",
                "message": "Unauthorized access"
            }), 403
            
        result = {
            "status": "success",
            "data": {
                "application_id": applicant.id,
                "submission_date": applicant.created_at.isoformat(),
                "status": "under_review",
                "last_updated": applicant.created_at.isoformat()
            }
        }
        
        # Store in cache
        cache.set(cache_key, result)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "status": "error",
        "message": ERROR_MESSAGES['rate_limit_exceeded']
    }), 429

@app.errorhandler(401)
def unauthorized_handler(e):
    return jsonify({
        "status": "error",
        "message": ERROR_MESSAGES['invalid_token']
    }), 401
