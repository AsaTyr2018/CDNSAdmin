from flask import Blueprint, jsonify, request
from . import zone_manager

bp = Blueprint('zones', __name__, url_prefix='/zones')


@bp.route('/', methods=['GET'])
def list_zones():
    zones = zone_manager.load_zones()
    return jsonify({'zones': zones})


@bp.route('/', methods=['POST'])
def create_zone():
    data = request.get_json(force=True)
    name = data.get('name')
    file_path = data.get('file')
    if not name or not file_path:
        return jsonify({'error': 'name and file are required'}), 400
    try:
        zone = zone_manager.add_zone(name, file_path)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(zone), 201


@bp.route('/<name>', methods=['DELETE'])
def remove_zone(name):
    if zone_manager.delete_zone(name):
        return '', 204
    return jsonify({'error': 'zone not found'}), 404


@bp.route('/<name>/enable', methods=['POST'])
def enable_zone(name):
    data = request.get_json(force=True)
    enabled = bool(data.get('enabled', True))
    if zone_manager.set_zone_enabled(name, enabled):
        return '', 204
    return jsonify({'error': 'zone not found'}), 404

