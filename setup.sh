#!/usr/bin/env bash
set -euo pipefail

# Install CDNSAdmin to /opt/CDNSAdmin using a Python virtual environment
TARGET_DIR="/opt/CDNSAdmin"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

sudo mkdir -p "$TARGET_DIR"

# copy repository files excluding the virtual environment if it already exists
sudo rsync -a --delete --exclude 'venv' "$REPO_DIR/" "$TARGET_DIR/"

# create virtual environment
if [ ! -d "$TARGET_DIR/venv" ]; then
    sudo python3 -m venv "$TARGET_DIR/venv"
fi

sudo "$TARGET_DIR/venv/bin/pip" install --upgrade pip
sudo "$TARGET_DIR/venv/bin/pip" install -r "$TARGET_DIR/requirements.txt"

echo "Installation completed. To run CDNSAdmin:"
echo "source $TARGET_DIR/venv/bin/activate && python $TARGET_DIR/app.py"
