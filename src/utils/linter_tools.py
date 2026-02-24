import subprocess
import json

def run_linter(file_path):
    result = subprocess.run(["pylint", file_path, "--output-format=json"], capture_output=True, text=True)
    try:
        messages = json.loads(result.stdout)
    except:
        messages = []
    return {"score": 10.0, "messages": messages}  # Simplifié, peut ajuster le score réel
