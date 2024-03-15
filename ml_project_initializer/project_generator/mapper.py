from django.http import HttpResponse
from .dto import GenerateProjectRequestDTO


def request_mapper(data) -> "GenerateProjectRequestDTO":
    required_fields = ['projectName', 'description', 'packageManager', 'modelType', 'packages']

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    return GenerateProjectRequestDTO(
        project_name=data['projectName'],
        description=data['description'],
        package_manager=data['packageManager'],
        model_type=data['modelType'],
        packages=data['packages']
    )


def response_mapper(zip_buffer, project_name):
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{project_name}.zip"'
    return response
