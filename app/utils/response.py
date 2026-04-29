from flask import jsonify

def success_response(data=None, message=None, status_code=200):
    """Format standard untuk response sukses."""
    response = {
        "success" : True,
        "data": data
    }

    if message:
        response["message"] = message

    return jsonify(response), status_code


def success_response_status(data=None, message=None, status_code=200):
    """Format standard untuk response sukses."""
    response = {
        "status" : "success",
        "data": data,
    }

    if message:
        response["message"] = message

    return jsonify(response), status_code

    

    
def error_response(message="Terjadi Kesalahan", errors=None, status_code=400):
    """Format standard untuk response error (termasuk validasi)."""
    response = {
        "success" : False,
        "message": message
    }

    if errors:
        response["errors"] = errors
        
    return jsonify(response), status_code

