from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def for_func(request):
    return render(request, 'for_func.html')


class ForClass(TemplateView):
    template_name = 'for_class.html'
    