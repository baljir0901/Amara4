import pytest
from app import app, db
from app.models import User, Applicant
import json

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create test user
            user = User(email="test@example.com")
            user.set_password("password123")
            db.session.add(user)
            db.session.commit()
        yield client
        
        with app.app_context():
            db.drop_all()

def test_login(client):
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json

def test_submit_application(client):
    # First login
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    token = response.json["access_token"]
    
    # Submit application
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "personal_info": {
            "name_kanji": "山田太郎",
            "name_furigana": "ヤマダタロウ",
            "birth_date": "1990-01-01",
            "gender": "male",
            "nationality": "日本"
        }
    }
    
    response = client.post("/api/v1/submit", 
        json=data, headers=headers)
    assert response.status_code == 201
    assert "application_id" in response.json

def test_rate_limit(client):
    # Test rate limiting
    for _ in range(6):
        response = client.post("/api/v1/auth/login", 
            json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 429

def test_cache(client):
    # Login
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    token = response.json["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Submit application
    data = {
        "personal_info": {
            "name_kanji": "山田太郎",
            "name_furigana": "ヤマダタロウ",
            "birth_date": "1990-01-01",
            "gender": "male",
            "nationality": "日本"
        }
    }

$apiTestsContent = @'
import pytest
from app import app, db
from app.models import User, Applicant
import json

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create test user
            user = User(email="test@example.com")
            user.set_password("password123")
            db.session.add(user)
            db.session.commit()
        yield client
        
        with app.app_context():
            db.drop_all()

def test_login(client):
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json

def test_submit_application(client):
    # First login
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    token = response.json["access_token"]
    
    # Submit application
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "personal_info": {
            "name_kanji": "山田太郎",
            "name_furigana": "ヤマダタロウ",
            "birth_date": "1990-01-01",
            "gender": "male",
            "nationality": "日本"
        }
    }
    
    response = client.post("/api/v1/submit", 
        json=data, headers=headers)
    assert response.status_code == 201
    assert "application_id" in response.json

def test_rate_limit(client):
    # Test rate limiting
    for _ in range(6):
        response = client.post("/api/v1/auth/login", 
            json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 429

def test_cache(client):
    # Login
    response = client.post("/api/v1/auth/login", 
        json={"email": "test@example.com", "password": "password123"})
    token = response.json["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Submit application
    data = {
        "personal_info": {
            "name_kanji": "山田太郎",
            "name_furigana": "ヤマダタロウ",
            "birth_date": "1990-01-01",
            "gender": "male",
            "nationality": "日本"
        }
    }
    response = client.post("/api/v1/submit", 
        json=data, headers=headers)
    app_id = response.json["application_id"]
    
    # Get application (should cache)
    response1 = client.get(f"/api/v1/application/{app_id}", 
        headers=headers)
    response2 = client.get(f"/api/v1/application/{app_id}", 
        headers=headers)
    assert response1.data == response2.data
