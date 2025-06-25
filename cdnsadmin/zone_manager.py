import json
import os
from typing import List, Dict


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
ZONES_FILE = os.path.join(DATA_DIR, 'zones.json')


def _ensure_storage() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(ZONES_FILE):
        with open(ZONES_FILE, 'w') as fh:
            json.dump([], fh)


def load_zones() -> List[Dict]:
    _ensure_storage()
    with open(ZONES_FILE) as fh:
        return json.load(fh)


def save_zones(zones: List[Dict]) -> None:
    _ensure_storage()
    with open(ZONES_FILE, 'w') as fh:
        json.dump(zones, fh, indent=2)


def add_zone(name: str, file_path: str) -> Dict:
    zones = load_zones()
    for z in zones:
        if z['name'] == name:
            raise ValueError('Zone already exists')
    zone = {
        'name': name,
        'file': file_path,
        'enabled': True
    }
    zones.append(zone)
    save_zones(zones)
    return zone


def delete_zone(name: str) -> bool:
    zones = load_zones()
    new_zones = [z for z in zones if z['name'] != name]
    if len(new_zones) == len(zones):
        return False
    save_zones(new_zones)
    return True


def set_zone_enabled(name: str, enabled: bool) -> bool:
    zones = load_zones()
    changed = False
    for z in zones:
        if z['name'] == name:
            z['enabled'] = enabled
            changed = True
            break
    if changed:
        save_zones(zones)
    return changed

