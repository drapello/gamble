from django.http import HttpResponse
from django.core.management import call_command

def crawl(request):
    call_command('run')
    html = "running"
    return HttpResponse(html)
    