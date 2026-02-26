#!/bin/bash

echo "Building Docker image..."
docker build -f deploy/docker/Dockerfile -t resume-analyzer .

echo "Running container..."
docker run -d -p 8001:8001 --name resume-analyzer resume-analyzer