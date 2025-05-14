#!/bin/bash

# Initialize Git repository
git init

# Add all files to Git
git add .

# Commit the changes
git commit -m "Initial commit of Django Gym Project"

# Rename the branch to main
git branch -M main

# Add the remote repository
git remote add origin https://github.com/Sadman-Shakib-Aungon/New-Project.git

# Push to GitHub
git push -u origin main

echo "Git setup complete!"
