from flask import Blueprint, request
from pydantic import ValidationError

from app.calc_example.schemas import CalcTeganganRequest
from app.calc_example.services import hitung_tegangan_baja
from app.utils.response import success_response, error_response

# Mendefinisikan blueprint dengan prefix /api/calc
calc_bp = Blueprint("calc", __name__, url_prefix="/api/calc/test")

@calc_bp.route("/tegangan", methods=["POST"])
def hitung_tegangan_endpoint():
    try:
        # Mengambil JSON payload
        json_data = request.get_json()
        if not json_data:
            return error_response("Payload wajib berupa JSON", status_code=400)

        # Validasi Pydantic
        validated_data = CalcTeganganRequest(**json_data)

        # Eksekusi kalkulasi ke service layer
        result = hitung_tegangan_baja(
            gaya_n=validated_data.gaya_newton, 
            luas_mm2=validated_data.luas_penampang_mm2
        )

        return success_response(data=result, message="Kalkulasi berhasil")

    except ValidationError as e:
        # Menangani error validasi dari Pydantic (contoh: input berupa string, atau angka <= 0)
        return error_response(
            message="Data tidak valid", 
            errors=e.errors(), 
            status_code=422
        )
    except Exception as e:
        # Menangani *internal server error* yang tidak terduga
        return error_response(message=f"Terjadi kesalahan server: {str(e)}", status_code=500)
    
