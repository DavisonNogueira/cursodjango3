from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola mundo') # Retorna como se fosse um template em HTML
