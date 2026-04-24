from flask import Blueprint, request, jsonify
from app.utils.response import success_response, error_response
from .schemas import OpeningPartInput
from .services import evaluate_pole_opening

opening_bp = Blueprint('opening_part', __name__, url_prefix='/api/opening-part')

@opening_bp.route('/calculate', methods=['POST'])
def calculate_opening():
    payload = request.get_json()
    
    try:
        # Validasi/mapping input ke Schema DTO
        input_data = OpeningPartInput(**payload)
        
        # Eksekusi orchestrator
        result = evaluate_pole_opening(input_data)
        
        # return jsonify(result), 200
        return success_response(data=result, message="Calculate Opening Part Success!")
    
        
    except TypeError as e:
        return jsonify({"error": "Data input tidak valid atau ada parameter yang hilang", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Terjadi kesalahan internal", "details": str(e)}), 500