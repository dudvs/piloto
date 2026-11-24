from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def sobre(request):
    return HttpResponse("Sobre o Sistema!")