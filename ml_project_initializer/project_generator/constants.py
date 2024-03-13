from django.conf import settings
import os

TEMPLATE_BASE_DIR = os.path.join(settings.BASE_DIR, 'project_generator', 'resource', 'template', 'project_name')
GENERATED_ZIP_DIR = os.path.join(settings.BASE_DIR, 'project_generator', 'resource', 'generated_zip')
GENERATED_BASE_DIR = os.path.join(settings.BASE_DIR, 'project_generator', 'resource', 'generated_template')
