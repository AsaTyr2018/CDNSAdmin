# CDNSAdmin

CDNSAdmin is a web-based administration interface for managing a CoreDNS deployment.
This project uses [Flask](https://flask.palletsprojects.com/) and is structured in a
modular way to allow extensions for zones, Corefile management and plugin handling.

## Development setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the development server:
   ```bash
   python app.py
   ```

After starting, open `http://localhost:5000` in your browser to verify the
application is running.
