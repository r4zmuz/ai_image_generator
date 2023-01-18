import os

def delete_json_files():
    # Get the directory of the main script
    main_script_dir = os.path.dirname(os.path.realpath(__file__))
    # Get the path to the responses folder
    directory_path = os.path.join(main_script_dir, "responses")
    # Get all files in the directory
    for filename in os.listdir(directory_path):
        # Check if file is a json file
        if filename.endswith(".json"):
            # Delete the json file
            os.remove(os.path.join(directory_path, filename))
