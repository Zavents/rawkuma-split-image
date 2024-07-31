import os
import re
from PIL import Image
import time

def split_and_rename_images(input_folder, output_folder, delay=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Sort files based on the numerical value in the filename
    files_with_numbers = [(filename, int(re.search(r'Net_(\d+)', filename).group(1)))
                          for filename in files
                          if re.search(r'Net_(\d+)', filename)]
    
    sorted_files = [filename for filename, _ in sorted(files_with_numbers, key=lambda x: x[1])]

    for index, filename in enumerate(sorted_files):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(input_folder, filename)
            image = Image.open(file_path)
            
            # Split the image into two halves
            width, height = image.size  
            left_half = image.crop((0, 0, width // 2, height))
            right_half = image.crop((width // 2, 0, width, height))
            
            # Save the right and left halves with new names
            right_half_index = index * 2
            left_half_index = right_half_index + 1
            right_half.save(os.path.join(output_folder, f'image_{right_half_index}.png'))
            left_half.save(os.path.join(output_folder, f'image_{left_half_index}.png'))




input_folder = r'YOUR_FOLDER_PATH'  # Folder containing the images to be split

output_folder = r'YOU_FOLDER_DESTINATION_PATH'  # Folder to save the split images
split_and_rename_images(input_folder, output_folder)  # Adding a delay of 1 second between processing each file
