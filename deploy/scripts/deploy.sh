#!/bin/bash

echo "Stopping old container (if exists)..."
docker stop resume-analyzer || true
docker rm resume-analyzer || true

echo "Building new image..."
docker build -f deploy/docker/Dockerfile -t resume-analyzer .

echo "Starting new container..."
docker run -d -p 8001:8001 --name resume-analyzer resume-analyzer

echo "Deployment complete."