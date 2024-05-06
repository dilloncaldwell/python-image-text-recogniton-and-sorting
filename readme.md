# Using Python to extract text from images and sort them

Requirements:

-   need python 3 installed `brew install python`
-   `pip3 install pytesseract --break-system-packages`
-   `brew install tesseract`
-   `pip3 install pillow`
-   `pip3 install opencv-python-headless --break-system-packages `

## The Problem

I normally have to sort images by hand, and I have a lot of images to sort for a football league with kids of different age groups and for multiple teams. Looking for a way to help automate this process of sorting the images by teams and age groups. The photos typically have the kids holding up a piece of paper saying their name, age group and team name. So trying to use tesseract to read that information add it to the image name and the filter the images by team and age group. Still a work in progress.

## Steps

1. Add the teams to `teams.py` teams array
2. Then the `preprocess_images.py` will run and prepare the images to extract text from them, and map the preprocess images to the original images
3. Then the `extract_text_from_image.py` will extract the text from the images and save a copy of the orginal images to the organized-images directory and append the name with the extracted text.
4. Then the `create_team_dirs.py` will create the directories for each team and move the images with matching names to the team directories. auto sorting them.
5. Then `mv_images_to_teams.py` will move the images from organized-images into matching teams directories using the extracted text.
6. Run `bash run_scripts.sh` to run these scripts in order.

## still a work in progress to increase accuracy
