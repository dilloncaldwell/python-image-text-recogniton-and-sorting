import os
from teams import teams  # Import teams array from teams.py

# Path to the directory where you want to create team directories
teams_directory = "teams"

# Function to create team directories
def create_team_directories(teams_directory, teams):
    # Create teams directory if it doesn't exist
    if not os.path.exists(teams_directory):
        os.makedirs(teams_directory)

    # Create directory for each team
    for team in teams:
        team_path = os.path.join(teams_directory, team)
        if not os.path.exists(team_path):
            os.makedirs(team_path)

# Call the function to create team directories
create_team_directories(teams_directory, teams)
