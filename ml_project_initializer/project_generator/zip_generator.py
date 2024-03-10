import zipfile
from .constants import GENERATED_PROJECT_BASE_DIR, GENERATED_ZIP_DIR
import os


def generate_zip(zip_file_name):
    zip_path = os.path.join(GENERATED_ZIP_DIR, zip_file_name)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(GENERATED_PROJECT_BASE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, GENERATED_PROJECT_BASE_DIR)
                zipf.write(file_path, arcname)
    return zip_path