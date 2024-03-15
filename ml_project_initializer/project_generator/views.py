from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .mapper import response_mapper, request_mapper
from .template_modifier import modify_template
from json import loads


@csrf_exempt
def generate_project(request):
    try:
        request_dto = request_mapper(loads(request.body))
        zip_buffer = modify_template(request_dto)
        return response_mapper(zip_buffer, request_dto.project_name)

    except ValueError as e:
        return HttpResponse(str(e), status=400)