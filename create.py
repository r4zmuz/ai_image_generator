import json
import os

import openai
from pathlib import Path




def create(PROMPT):
    DATA_DIR = Path.cwd() / "responses"
    DATA_DIR.mkdir(exist_ok=True)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    openai.api_key_path = os.path.join(dir_path, "api_key.txt")

    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
        response_format="b64_json",
    )

    file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)

