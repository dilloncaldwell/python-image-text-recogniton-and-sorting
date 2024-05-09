import os
import cv2
import pytesseract
import json
import shutil

# Path to the directory containing the preprocessed images
preprocessed_images_directory = "preprocessed-images"

# Path to the directory containing the original images
original_images_directory = "original-images"

# Path to the directory where organized images will be saved
organized_images_directory = "organized-images"

# Load the mapping dictionary from the image_mapping.json file
mapping_file = os.path.join(preprocessed_images_directory, "image_mapping.json")
with open(mapping_file, 'r') as f:
    image_mapping = json.load(f)

# Function to extract text from images using Tesseract OCR
def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    extracted_text = pytesseract.image_to_string(img, config='--user-words wordlist.txt')
    return extracted_text.strip()

# Function to update filenames in the organized images directory
def update_filenames(organized_images_directory):
    # Check if the organized images directory exists, if not, create it
    if not os.path.exists(organized_images_directory):
        os.makedirs(organized_images_directory)
    
    # Loop through each original image file
    for original_file, preprocessed_file in image_mapping.items():
        preprocessed_path = os.path.join(preprocessed_images_directory, preprocessed_file)
        extracted_text = extract_text_from_image(preprocessed_path)
        new_filename = f"{os.path.splitext(original_file)[0]}_{extracted_text}.jpg"
        original_path = os.path.join(original_images_directory, original_file)
        new_path = os.path.join(organized_images_directory, new_filename)
        shutil.copy(original_path, new_path)
        print(f"File '{original_file}' renamed and copied to '{new_path}'")

# Call the function to update filenames in the organized images directory
update_filenames(organized_images_directory)
