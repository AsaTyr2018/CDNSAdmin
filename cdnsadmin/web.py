from flask import Blueprint, render_template, request, redirect, url_for, flash

from . import zone_manager, backend

bp = Blueprint('web', __name__)


@bp.route('/')
def index():
    zones = zone_manager.load_zones()
    backend_cfg = backend.load_config()
    return render_template('index.html', zones=zones, backend=backend_cfg)


@bp.route('/zones/add', methods=['POST'])
def add_zone():
    name = request.form.get('name')
    file_path = request.form.get('file')
    if not name or not file_path:
        flash('Name and file are required', 'danger')
        return redirect(url_for('web.index'))
    try:
        zone_manager.add_zone(name, file_path)
        flash('Zone added', 'success')
    except ValueError as e:
        flash(str(e), 'danger')
    return redirect(url_for('web.index'))


@bp.route('/zones/<name>/delete', methods=['POST'])
def delete_zone(name: str):
    if zone_manager.delete_zone(name):
        flash('Zone deleted', 'success')
    else:
        flash('Zone not found', 'danger')
    return redirect(url_for('web.index'))


@bp.route('/zones/<name>/enable', methods=['POST'])
def toggle_zone(name: str):
    enabled = bool(request.form.get('enabled'))
    if zone_manager.set_zone_enabled(name, enabled):
        flash('Zone updated', 'success')
    else:
        flash('Zone not found', 'danger')
    return redirect(url_for('web.index'))
