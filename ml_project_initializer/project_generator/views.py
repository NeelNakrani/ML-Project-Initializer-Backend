from django.shortcuts import render
from django.http import HttpResponse
from .dto import GenerateProjectRequestDTO
from .template_modifier import modify_template
from .zip_generator import generate_zip
import json
from constants import GENERATED_ZIP_DIR

# Create your views here.
def generate_project(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dto = GenerateProjectRequestDTO.validate(data)
            modify_template(dto)
            zip_file_name = f"{dto.project_name}.zip"
            with open(generate_zip(zip_file_name)) as zipf:
                response = HttpResponse(zipf.read(), content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename={zip_file_name}'
                return response

        except ValueError as e:
            return HttpResponse(str(e), status=400)
    else:
        return HttpResponse('Method not allowed', status=405)