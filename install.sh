#!/bin/bash
echo "Installing packages..."

pip install -r requirements.txt

echo "Installation complete."
read -p "Press any key to exit..." -n1 -s
echo
