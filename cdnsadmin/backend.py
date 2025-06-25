from flask import Blueprint, jsonify, request
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CONFIG_FILE = os.path.join(DATA_DIR, 'config.json')


def _ensure_storage() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as fh:
            json.dump({}, fh)


def load_config() -> dict:
    _ensure_storage()
    with open(CONFIG_FILE) as fh:
        return json.load(fh)


def save_config(config: dict) -> None:
    _ensure_storage()
    with open(CONFIG_FILE, 'w') as fh:
        json.dump(config, fh, indent=2)


bp = Blueprint('connect', __name__, url_prefix='/connect')


@bp.route('/', methods=['POST'])
def connect():
    data = request.get_json(force=True)
    host = data.get('host')
    port = data.get('port', 53)
    if not host:
        return jsonify({'error': 'host is required'}), 400
    config = {'host': host, 'port': port}
    save_config(config)
    return jsonify(config), 200


@bp.route('/', methods=['GET'])
def get_config():
    config = load_config()
    return jsonify(config)
