#!/bin/bash
# Initialize git repository
git init
# Add all files
git add .
# Commit changes
git commit -m "Initial commit of Django Gym Project"
# Set main branch
git branch -M main
# Add remote repository
git remote add origin https://github.com/Sadman-Shakib-Aungon/New-Project.git
# Push to GitHub
git push -u origin main
