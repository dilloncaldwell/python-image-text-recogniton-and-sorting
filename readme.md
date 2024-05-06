# Using Python to extract text from images and sort them

Requirements:

-   need python 3 installed `brew install python`
-   `pip3 install pytesseract --break-system-packages`
-   `brew install tesseract`
-   `pip3 install pillow`
-   `pip3 install opencv-python-headless --break-system-packages `

## Steps

1. Add the teams to `teams.py` teams array
2. Then the `preprocess_images.py` will run and prepare the images to extract text from them, and map the preprocess images to the original images
3. Then the `extract_text_from_image.py` will extract the text from the images and save a copy of the orginal images to the organized-images directory and append the name with the extracted text.
4. Then the `create_team_dirs.py` will create the directories for each team and move the images with matching names to the team directories. auto sorting them.

## still a work in progress to increase accuracy
