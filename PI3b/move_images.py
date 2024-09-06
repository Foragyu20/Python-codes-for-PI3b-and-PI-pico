import os
import shutil
from glob import glob

# List of raster image formats to search for (excluding BMP)
raster_image_formats = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.tiff', '*.webp']

# Define the source directory (root directory where the search will start)
source_directory = '/storage/emulated/0'

# Define the destination directory
destination_directory = os.path.join(source_directory, 'images')

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Search for all raster image files except BMP
for image_format in raster_image_formats:
    # Use glob to find all files matching the pattern in the source directory and its subfolders
    for filepath in glob(os.path.join(source_directory, '**', image_format), recursive=True):
        try:
            # Move the file to the destination directory
            shutil.move(filepath, destination_directory)
            print(f"Moved: {filepath}")
        except Exception as e:
            print(f"Error moving {filepath}: {e}")

print("Image files moved successfully.")
