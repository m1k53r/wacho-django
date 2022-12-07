from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello world")


def damn(request):
    return JsonResponse({"test": "aaa"})
