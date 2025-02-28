from main.utils import menu
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
def get_menu_context(request:HttpRequest):
    return {'main':menu}

