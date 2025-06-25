# CDNSAdmin

CDNSAdmin is a web-based administration interface for managing a CoreDNS deployment. This project uses [Flask](https://flask.palletsprojects.com/) and is structured in a modular way to allow extensions for zones, Corefile management and plugin handling.

## Development setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the development server:
   ```bash
   python app.py
   ```

After starting, open `http://<server-ip>:5000` in your browser to verify the application is running.
The server listens on `0.0.0.0` by default so it is reachable from your LAN.

## Zone management API

The first management module allows basic CRUD operations for zones. All routes are prefixed with `/zones`.

* `GET /zones/` – list all configured zones.
* `POST /zones/` – add a new zone. Send JSON with `name` and `file`.
* `DELETE /zones/<name>` – remove a zone by name.
* `POST /zones/<name>/enable` – toggle zone activation with JSON `{ "enabled": true }`.

Zone information is stored in `data/zones.json` and can be edited via the API.

## Backend connection API

CDNSAdmin can store the address of a real CoreDNS server that should be used as
a backend. Use the `/connect` endpoint to configure this server:

* `POST /connect/` – set the backend host and optional port with JSON
  `{ "host": "1.2.3.4", "port": 1053 }`.
* `GET /connect/` – retrieve the currently configured backend connection.

The connection configuration is saved in `data/config.json`.

## Automated installation

For a system-wide deployment, run the provided `setup.sh` script. It copies the
repository to `/opt/CDNSAdmin` and installs the Python requirements in a
virtual environment:

```bash
sudo ./setup.sh
```

After installation activate the environment and start the application:

```bash
source /opt/CDNSAdmin/venv/bin/activate
python /opt/CDNSAdmin/app.py
```
