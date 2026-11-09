import json
import subprocess
from pathlib import Path

def get_key(keyname: str):
    with open("keys.json") as f:
            data = json.load(f)
            return data[keyname]

def extract_flight_record(file_name: str, output_format: str, dji_key: str) -> int:
    """
    Extracts txt file from data/input/{file_name}.txt and extracts it in dat/output/{file_name}/{output_format}
    """
    output_format = "json"
    input_path = f"data/input/{file_name}.txt"
    if not Path(input_path).exists:
         print(f"File {input_path} doesn't exist")
         return 1
    
    output_path = f"data/output/{file_name}.{output_format}"

    if Path(output_path).exists:
         print(f"Skipping File {output_path} as it already exists")
         return 0

    subprocess.run(["djirecord", input_path, f"--{output_format}", "-o", output_path, "--api-key", dji_key])

    return 0


