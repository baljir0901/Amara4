import pytest
from app import app, db
from app.models import Applicant

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    rv = client.get("/")
    assert rv.status_code == 200

def test_form_submission(client):
    data = {
        "name_kanji": "山田太郎",
        "name_furigana": "ヤマダタロウ",
        "birth_date": "1990-01-01",
        "gender": "male",
        "nationality": "日本"
    }
    rv = client.post("/", data=data)
    assert rv.status_code in [200, 302]
