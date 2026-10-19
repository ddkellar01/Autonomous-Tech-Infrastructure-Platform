#!/bin/bash
set -e

echo "Starting Autonomous Tech & Infrastructure Engine..."

# Initialize database or config folders if missing
mkdir -p /app/config
mkdir -p /app/models

# Execute main process
exec python -m src.core.engine
