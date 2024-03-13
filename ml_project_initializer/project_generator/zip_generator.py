import zipfile
from .constants import GENERATED_ZIP_DIR
import os
import io


def generate_zip(directory_to_zip, zip_file_name):
    zip_path = os.path.join(GENERATED_ZIP_DIR, zip_file_name)
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_to_zip):
            # Add directory (including empty ones) to the zip file
            for dir in _:
                dir_path = os.path.join(root, dir)
                # Calculate the archive name path, and ensure it has a trailing slash
                arcname = os.path.relpath(dir_path, start=directory_to_zip) + '/'
                # Use writestr to create a directory in the zip file
                zipf.writestr(arcname, '')

            for file in files:
                file_path = os.path.join(root, file)
                # Calculate relative archive name path.
                arcname = os.path.relpath(file_path, start=directory_to_zip)
                zipf.write(file_path, arcname)
    zip_buffer.seek(0)
    return zip_buffer
