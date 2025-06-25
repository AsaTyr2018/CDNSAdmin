from flask import Blueprint, jsonify

bp = Blueprint('zones', __name__, url_prefix='/zones')

@bp.route('/')
def list_zones():
    # Placeholder implementation
    return jsonify({'zones': []})
