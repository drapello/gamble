from django.http import HttpResponse


def quemfaz(request):
    html = "up"
    return HttpResponse(html)