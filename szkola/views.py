from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.template import loader


class Lesson:
    def __init__(self, name, lecturer):
        self.name = name
        self.lecturer = lecturer


def index(request: HttpRequest):
    lessons = [{"name": "polish",
                "lecturer": "Sienkiewicz"},
               {"name": "maths",
                "lecturer": "Niewulis"},
               {"name": "english",
                "lecturer": "Wengrzyn"}]

    betterLessons = [Lesson("polish", "Sienkiewicz"),
                     Lesson("maths", "Niewulis"),
                     Lesson("english", "Wengrzyn")]

    context = {
        'welcome_message': request.GET['welcome'],
        'lessons': betterLessons,
    }

    return render(request, 'szkola/index.html', context)


def damn(request: HttpRequest):
    data = ""
    if "user_id" in request.GET:
        data = request.GET['user_id']

    return JsonResponse({"test": data})
