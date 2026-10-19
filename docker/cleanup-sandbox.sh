#!/bin/bash
# Cleans up dangling ephemeral containers and unused sandbox images to free system resources

echo "Cleaning up stopped sandbox containers..."
docker container prune -f

echo "Pruning dangling builder cache..."
docker builder prune -f

echo "Sandbox cleanup completed successfully."
