import os

SANDBOX_DIR = "./sandbox"

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(file_path, content):
    # Sécurité : n'autorise que sandbox
    if not file_path.startswith(SANDBOX_DIR):
        raise PermissionError("Vous ne pouvez écrire qu'à l'intérieur de sandbox")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
