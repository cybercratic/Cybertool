#!/bin/bash

echo "🔧 Installing CyberTool dependencies..."

pkg update -y
pkg install python -y
pip install --upgrade pip

pip install pyfiglet colorama requests

echo "✅ All dependencies installed!"
echo "👉 Now run: python cybertool.py <ip>"
