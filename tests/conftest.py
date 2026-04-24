import pytest
from app import create_app

@pytest.fixture
def app():
    # Membuat instance aplikasi untuk testing
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    # Memaksa Flask masuk ke dalam application context
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    # Menggunakan "with" untuk test_client
    # Ini menjamin request state selalu dibersihkan (teardown) setelah tiap test
    with app.test_client() as client:
        yield client