import os
import shutil
from teams import teams  # Import teams array from teams.py

# Path to the directory containing the organized images
organized_directory = "organized-images"

# Path to the directory where team directories are located
teams_directory = "teams"

# Function to move images to team directories
def move_images_to_team_directories(organized_directory, teams_directory):
    # Loop through each image in the organized directory
    for image_file in os.listdir(organized_directory):
        image_path = os.path.join(organized_directory, image_file)
        if os.path.isfile(image_path):
            # Extract team name from the filename
            team_name = extract_team_name(image_file)

            # Search for team name within full name
            for team in teams:
                if team in team_name.lower():
                    # If team directory exists, move the image to that directory
                    team_directory = os.path.join(teams_directory, team)
                    if os.path.exists(team_directory):
                        shutil.move(image_path, os.path.join(team_directory, image_file))
                    else:
                        print(f"Team directory '{team}' does not exist.")

# Function to extract team name from filename
def extract_team_name(filename):
    # Remove file extension
    name_without_extension = os.path.splitext(filename)[0]
    # Remove hyphens and split the name into parts
    parts = name_without_extension.split("-")
    # Concatenate parts to form the full name
    team_name = " ".join(parts)
    return team_name

# Call the function to move images to team directories
move_images_to_team_directories(organized_directory, teams_directory)
