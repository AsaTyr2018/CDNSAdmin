from flask import Blueprint, jsonify

bp = Blueprint('plugins', __name__, url_prefix='/plugins')

@bp.route('/')
def list_plugins():
    # Placeholder implementation
    return jsonify({'plugins': []})
