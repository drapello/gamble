from django.http import HttpResponse

def new(request):
    html = "up"
    return HttpResponse(html)