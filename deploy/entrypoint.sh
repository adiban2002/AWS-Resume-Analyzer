#!/bin/bash

echo "Starting AWS Resume Analyzer..."

uvicorn app.main:app --host 0.0.0.0 --port 8001