import helpers
import subprocess

api_keys =helpers.get_keys()
dji_key = api_keys["DJI_API"]

file_name = "FlightRecord_2026-11-06_[10-59-44]"

output_format = "json"
input_path = f"data/input/{file_name}.txt"
output_path = f"data/output/{file_name}.{output_format}"

subprocess.run(["djirecord", input_path, f"--{output_format}", "-o", output_path, "--api-key", dji_key])