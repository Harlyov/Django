from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'common/home.html'





def custom_404_view(request,exception):
    return render(request, 'common/404.html', status=404)