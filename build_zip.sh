#!/bin/bash
set -e
ROOT_DIR=$(pwd)
NAME="OpenSource-Chatbot-Automation"
ZIP_NAME="$NAME.zip"
rm -f "$ZIP_NAME"
zip -r "$ZIP_NAME" README.md LICENSE requirements.txt Dockerfile sample_config.yaml src scripts .github
echo "Created $ZIP_NAME"
