#!/bin/bash

# Create a temporary directory
mkdir -p /tmp/gym_temp

# Copy all our files to the temporary directory
cp -r * /tmp/gym_temp/

# Clone the GitHub repository
git clone https://github.com/Sadman-Shakib-Aungon/New-Project.git /tmp/new_project

# Copy our files to the cloned repository
cp -r /tmp/gym_temp/* /tmp/new_project/

# Change to the cloned repository directory
cd /tmp/new_project

# Add all files to Git
git add .

# Commit the changes
git commit -m "Add Django Gym Project"

# Push to GitHub
git push

echo "Files copied and pushed to GitHub!"
