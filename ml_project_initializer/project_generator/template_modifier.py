from .constants import TEMPLATE_BASE_DIR, GENERATED_BASE_DIR
import shutil
import os
import uuid
from datetime import datetime
from .dto import GenerateProjectRequestDTO
from .zip_generator import generate_zip


def copy_template_to_generated_dir(project_name):
    unique_id = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(uuid.uuid4())
    destination_dir_name = f"{project_name}_{unique_id}"
    destination_dir = os.path.join(GENERATED_BASE_DIR, destination_dir_name)
    shutil.copytree(TEMPLATE_BASE_DIR, destination_dir)
    return destination_dir

def modify_project_description(destination_dir, description):
    readme_path = os.path.join(destination_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(description)


def add_packages_to_requirements(destination_dir, packages):
    requirements_path = os.path.join(destination_dir, "requirements.txt")

    with open(requirements_path, "a") as requirements_file:
        for package in packages:
            requirements_file.write(f"{package}\n")


def delete_generated_template(destination_dir):
    print(destination_dir)
    if os.path.exists(destination_dir) and os.path.isdir(destination_dir):
        shutil.rmtree(destination_dir)
        print(f"Deleted generated template directory: {destination_dir}")
    else:
        print("Directory does not exist or is not a directory.")


def generate_script_files(destination_dir, package_manager):
    # Define the paths for the setup files
    setup_pip_sh = os.path.join(destination_dir, 'setup_pip.sh')
    setup_conda_sh = os.path.join(destination_dir, 'setup_conda.sh')
    setup_pip_bat = os.path.join(destination_dir, 'setup_pip.bat')
    setup_conda_bat = os.path.join(destination_dir, 'setup_conda.bat')

    if package_manager == 'pip':
        # If pip is chosen, delete the conda files and rename pip files
        os.remove(setup_conda_sh)
        os.rename(setup_pip_sh, os.path.join(destination_dir, 'setup.sh'))
        os.remove(setup_conda_bat)
        os.rename(setup_pip_bat, os.path.join(destination_dir, 'setup.bat'))
    elif package_manager == 'conda':
        # If conda is chosen, delete the pip files and rename conda files
        os.remove(setup_pip_sh)
        os.rename(setup_conda_sh, os.path.join(destination_dir, 'setup.sh'))
        os.remove(setup_pip_bat)
        os.rename(setup_conda_bat, os.path.join(destination_dir, 'setup.bat'))

def modify_template(dto: GenerateProjectRequestDTO):
    destination_dir = copy_template_to_generated_dir(dto.project_name)
    modify_project_description(destination_dir, dto.description)
    add_packages_to_requirements(destination_dir, dto.packages)
    generate_script_files(destination_dir, dto.package_manager)

    # Generate zip file of the modified template
    zip_file_name = f"{dto.project_name}.zip"
    zip_buffer = generate_zip(destination_dir, zip_file_name)

    #  todo: change scripting files, generate zip
    delete_generated_template(destination_dir)
    return zip_buffer