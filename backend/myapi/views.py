import json

from django.http import HttpResponse


def page_not_found_view(request, exception):
    return HttpResponse(json.dumps({
        "error": '경로가 잘못됨',
    }), content_type='application/json', status=404)
