from flask import Blueprint, request, jsonify
from app.utils.response import success_response, error_response, success_response_status
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
        # print(type(result))
        return success_response(data=result)
    
        
    except TypeError as e:
        return error_response(errors=e.args, status_code=400)
    except Exception as e:
        return error_response(errors=e.args, status_code=500)
    

@opening_bp.route('/calculate-status', methods=['POST'])
def calculate_opening_status():
    payload = request.get_json()
    
    try:
        # Validasi/mapping input ke Schema DTO
        input_data = OpeningPartInput(**payload)
        
        # Eksekusi orchestrator
        result = evaluate_pole_opening(data=input_data, type=1)
        
        # return jsonify(result), 200
        # print(type(result))
        return success_response_status(data=result)
    
        
    except TypeError as e:
        return error_response(errors=e.args, status_code=400)
    except Exception as e:
        return error_response(errors=e.args, status_code=500)