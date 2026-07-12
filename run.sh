#!/usr/bin/env bash
# GPX Entry Point Wrapper

# 1. Find the directory where this repository was cloned by gpx
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 2. Move into that directory so the app can find its local files
cd "$DIR" || exit 1

# 3. Launch the actual application (Modify this line for your specific project)
# Example for a Python project:
python3 your_actual_script.py "$@"

# Example for a Node.js project:
# node index.js "$@"
