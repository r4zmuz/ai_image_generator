import os
import json
import base64
from io import BytesIO

from PIL import Image

def decode_json_files():
    # Get the directory of the main script
    main_script_dir = os.path.dirname(os.path.realpath(__file__))
    # Get the path to the responses folder
    directory_path = os.path.join(main_script_dir, "responses")
    # Get all files in the directory
    for filename in os.listdir(directory_path):
        # Check if file is a json file
        if filename.endswith(".json"):
            # Open the json file
            with open(os.path.join(directory_path, filename), "r") as json_file:
                data = json.load(json_file)
            # Decode the image data from json
            image_data = base64.b64decode(data["data"][0]["b64_json"])
            # Create a PIL Image object
            image = Image.open(BytesIO(image_data))
            # Create a new file name by changing the extension to png
            new_file_name = f"{data['created']}.png"
            # Save the image in png format
            image.save(os.path.join(directory_path, new_file_name), "PNG")
