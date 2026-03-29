from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from django.http import HttpResponseServerError

class HomeView(TemplateView):
    template_name = 'common/home.html'





def custom_404_view(request,exception):
    return render(request, 'common/404.html', status=404)


def custom_500_view(request):
    return render(request, 'common/500.html', status=500)
