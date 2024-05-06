# import os
# from PIL import Image
# import pytesseract
# import shutil
# import re

# # Path to the directory containing your images
# images_directory = "preprocessed-images"

# # Path to the directory where you want to organize the images
# organized_directory = "organized-images"

# # Function to extract text from an image using Tesseract OCR
# def extract_text_from_image(image_path):
#     img = Image.open(image_path)
#     extracted_text = pytesseract.image_to_string(img)
#     return extracted_text.strip()

# # Function to generate a safe filename from the extracted text
# def generate_safe_filename(text):
#     # Replace non-alphanumeric characters with hyphens
#     safe_text = re.sub(r'\W+', '-', text)
#     return safe_text.lower()  # Convert to lowercase


# # Function to copy images to the organized directory with new names based on extracted text
# def copy_images_with_new_names(images_directory, organized_directory):
#     # Create organized directory if it doesn't exist
#     if not os.path.exists(organized_directory):
#         os.makedirs(organized_directory)

#     # Loop through each image in the images directory
#     for image_file in os.listdir(images_directory):
#         image_path = os.path.join(images_directory, image_file)
#         if os.path.isfile(image_path):
#             # Check if the file is a valid image file
#             try:
#                 Image.open(image_path)
#             except (IOError, OSError):
#                 print(f"Skipping non-image file: {image_path}")
#                 continue

#             # Extract text from the image
#             extracted_text = extract_text_from_image(image_path)

#             # Generate new filename based on extracted text
#             safe_filename = generate_safe_filename(extracted_text)
#             # new_filename = f"{safe_filename}.jpg"  # You can adjust the file extension if needed
#             # Append extracted text to the original filename
#             filename, file_extension = os.path.splitext(image_file)
#             new_filename = f"{filename}_{safe_filename}{file_extension}"

#             # Copy the image to the organized directory with the new filename
#             shutil.copy(image_path, os.path.join(organized_directory, new_filename))

# # Call the function to copy images with new names based on extracted text
# copy_images_with_new_names(images_directory, organized_directory)

# import os
# import cv2
# import pytesseract
# import json
# from PIL import Image
# import shutil

# # Path to the directory containing the preprocessed images
# preprocessed_images_directory = "preprocessed-images"

# # Path to the directory where organized images will be saved
# organized_images_directory = "organized-images"

# # Load the mapping dictionary from the image_mapping.json file
# mapping_file = os.path.join(preprocessed_images_directory, "image_mapping.json")
# with open(mapping_file, 'r') as f:
#     image_mapping = json.load(f)
# # Print the loaded image mapping dictionary
# print("Loaded image mapping:", image_mapping)
# # Function to extract text from images using Tesseract OCR
# def extract_text_from_image(image_path):
#     img = cv2.imread(image_path)
#     extracted_text = pytesseract.image_to_string(img)
#     return extracted_text.strip()

# # Function to update filenames in the organized images directory
# def update_filenames(organized_images_directory):
#     # Check if the organized images directory exists, if not, create it
#     if not os.path.exists(organized_images_directory):
#         print("Error: Organized images directory does not exist. Creating Directory...")
#         os.makedirs(organized_images_directory)
    
#     # Loop through each image in the organized directory
#     for organized_file in os.listdir(organized_images_directory):
#         print("Processing file:", organized_file)
#         original_filename = image_mapping.get(organized_file)
#         if original_filename:
#             original_path = os.path.join(preprocessed_images_directory, original_filename)
#             new_filename = f"{os.path.splitext(organized_file)[0]}_{extract_text_from_image(original_path)}.jpg"
#             new_filepath = os.path.join(organized_images_directory, new_filename)
#             print(f"Copying '{original_path}' to '{new_filepath}'")
#             shutil.copy(original_path, new_filepath)

# # Call the function to update filenames in the organized images directory
# update_filenames(organized_images_directory)

# print("Filenames in the organized images directory updated.")

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
