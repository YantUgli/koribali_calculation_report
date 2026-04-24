from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    """Format standard untuk response sukses."""
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code

def error_response(message="Error", errors=None, status_code=400):
    """Format standard untuk response error (termasuk validasi)."""
    response = {
        "status": "error",
        "message": message
    }
    if errors:
        response["errors"] = errors
        
    return jsonify(response), status_code