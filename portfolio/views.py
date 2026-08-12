from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, I am building my portfolio!")