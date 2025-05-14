import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print the output"""
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stderr)
        return False

def main():
    """Main function to connect to GitHub"""
    # Initialize Git repository
    if not run_command("git init"):
        return

    # Add all files to Git
    if not run_command("git add ."):
        return

    # Commit the changes
    if not run_command('git commit -m "Initial commit of Django Gym Project"'):
        return

    # Rename the branch to main
    if not run_command("git branch -M main"):
        return

    # Add the remote repository
    if not run_command("git remote add origin https://github.com/Sadman-Shakib-Aungon/New-Project.git"):
        return

    # Push to GitHub
    if not run_command("git push -u origin main"):
        print("Note: If you're getting authentication errors, you may need to set up a personal access token.")
        print("Visit: https://github.com/settings/tokens to create a token.")
        print("Then use: git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/Sadman-Shakib-Aungon/New-Project.git")
        return

    print("Successfully connected to GitHub!")

if __name__ == "__main__":
    main()
