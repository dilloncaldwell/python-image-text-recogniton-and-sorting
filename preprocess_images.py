import os
import cv2
import json

# Path to the directory containing the original images
original_images_directory = "original-images"

# Path to the directory where preprocessed images will be saved
preprocessed_images_directory = "preprocessed-images"

# Create a mapping dictionary to map preprocessed image filenames to original image filenames
image_mapping = {}

# Create preprocessed images directory if it doesn't exist
if not os.path.exists(preprocessed_images_directory):
  os.makedirs(preprocessed_images_directory)

# Function to preprocess images
def preprocess_images(original_images_directory, preprocessed_images_directory):
  # Loop through each image in the original directory
  for image_file in os.listdir(original_images_directory):
    if image_file.endswith(('.jpg', '.JPG', '.jpeg', '.png')): 
      original_path = os.path.join(original_images_directory, image_file)
      preprocessed_filename = f"{os.path.splitext(image_file)[0]}.jpg"
      preprocessed_path = os.path.join(preprocessed_images_directory, preprocessed_filename)
      try:
        # Read the original image
        original_image = cv2.imread(original_path)
        # Check if the image is empty or invalid
        if original_image is None:
          print(f"Failed to read image: {image_file}")
          continue
        # Upscale the preprocessed image to 200%
        scaled_image = cv2.resize(original_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # Convert the original image to grayscale
        gray = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
        # Apply binarization
        # _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # Apply denoising
        denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
        # tiff_path = os.path.join(preprocessed_images_directory, tiff_filename)
        cv2.imwrite(preprocessed_path, denoised)
        # Add the mapping from preprocessed image filename to original image filename
        image_mapping[image_file] = preprocessed_filename
      except Exception as e:
        print(f"Error preprocessing image {image_file}: {e}")
    # Save the mapping dictionary to a JSON file
    mapping_file = os.path.join(preprocessed_images_directory, "image_mapping.json")
    with open(mapping_file, 'w') as f:
      json.dump(image_mapping, f)
# Call the function to preprocess images
preprocess_images(original_images_directory, preprocessed_images_directory)
print("Preprocessing completed.")
