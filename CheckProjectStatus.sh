#!/bin/bash

# Check project directory
PROJECT_DIR="/home/levent/Desktop/Project/DIY_WakeUpLightProject"

# Switch to the project directory
cd "$PROJECT_DIR" || { echo "Project directory not found! Exiting."; exit 1; }

# Check git updates
echo "Checking the status of the project repository..."

# synchronise changes
git fetch origin

# check the changes
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/main)

if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
    echo "Remote repository is ahead. Pulling the latest changes..."
    git pull origin main
else
    echo "Nothing has changed, everything is up-to-date."
fi
