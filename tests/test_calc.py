def test_hitung_tegangan_sukses_dan_aman(client):
    # Mengirim payload yang menghasilkan tegangan aktual (10000 / 100 = 100 MPa)
    # Tegangan izin adalah 240 / 1.5 = 160 MPa (Seharusnya AMAN)
    payload = {
        "gaya_newton": 10000.0,
        "luas_penampang_mm2": 100.0
    }
    
    response = client.post("/api/calc/test/tegangan", json=payload)
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"]["tegangan_aktual_mpa"] == 100.0
    assert data["data"]["status"] == "Aman"

def test_hitung_tegangan_sukses_dan_tidak_aman(client):
    # Menghasilkan tegangan 200 MPa (Melebihi batas izin 160 MPa)
    payload = {
        "gaya_newton": 20000.0,
        "luas_penampang_mm2": 100.0
    }
    
    response = client.post("/api/calc/test/tegangan", json=payload)
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"]["status"] == "Tidak Aman (Melebihi Tegangan Izin)"

def test_hitung_tegangan_error_validasi(client):
    # Gaya tidak boleh minus berdasarkan aturan schema.py (gt=0)
    payload = {
        "gaya_newton": -500,
        "luas_penampang_mm2": 100.0
    }
    
    response = client.post("/api/calc/test/tegangan", json=payload)
    data = response.get_json()

    assert response.status_code == 422
    assert data["status"] == "error"
    assert "errors" in data