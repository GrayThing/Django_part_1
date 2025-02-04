from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def for_func(request):
    return render(request, 'second_task/for_func.html')


class ForClass(TemplateView):
    template_name = 'second_task/for_class.html'
    