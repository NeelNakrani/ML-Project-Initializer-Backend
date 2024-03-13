from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .dto import GenerateProjectRequestDTO
from .template_modifier import modify_template
from .zip_generator import generate_zip
import json
from .constants import GENERATED_ZIP_DIR

@csrf_exempt
def generate_project(request):
    try:
        print('request')
        data = json.loads(request.body)
        dto = GenerateProjectRequestDTO.validate(data)

        zip_buffer = modify_template(dto)
        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{dto.project_name}.zip"'
        return response

    except ValueError as e:
        return HttpResponse(str(e), status=400)