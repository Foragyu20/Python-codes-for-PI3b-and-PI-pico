import os
import shutil
from glob import glob

# List of raster image formats to search for (excluding BMP)
raster_image_formats = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.tiff', '*.webp']

# List of video formats to search for (excluding AVI)
video_formats = ['*.mp4', '*.mkv', '*.mov', '*.avi','*.webm']

# Define the source directory (root directory where the search will start)
source_directory = '/storage/emulated/0'

# Define the destination directories
images_directory = os.path.join(source_directory, 'images')
videos_directory = os.path.join(source_directory, 'videos')

# Create the destination directories if they don't exist
os.makedirs(images_directory, exist_ok=True)
os.makedirs(videos_directory, exist_ok=True)

# Function to move files
def move_files(file_patterns, destination_dir):
    for file_pattern in file_patterns:
        # Use glob to find all files matching the pattern in the source directory and its subfolders
        for filepath in glob(os.path.join(source_directory, '**', file_pattern), recursive=True):
            try:
                # Move the file to the destination directory
                shutil.move(filepath, destination_dir)
                print(f"Moved: {filepath}")
            except Exception as e:
                print(f"Error moving {filepath}: {e}")

# Move image files
move_files(raster_image_formats, images_directory)

# Move video files
move_files(video_formats, videos_directory)

print("Image and video files moved successfully.")
