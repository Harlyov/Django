from django.shortcuts import render

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from fans.forms import FanForm
from fans.models import Fan

class FanCreateView(CreateView):
    model = Fan
    form_class = FanForm
    template_name = 'fans/fan_create.html'
    success_url = reverse_lazy('fans:list')

    def form_valid(self, form):
        messages.success(self.request, 'Fan successfully created!')
        return super().form_valid(form)


class FanUpdateView(UpdateView):
    model = Fan
    form_class = FanForm
    template_name = 'fans/fan_update.html'
    success_url = reverse_lazy('fans:list')

    def form_valid(self, form):
        messages.success(self.request, 'Fan successfully updated!')
        return super().form_valid(form)




class FanListView(ListView):
    model = Fan
    template_name = 'fans/fan_list.html'
    context_object_name = 'fans'




class FanDeleteView(DeleteView):
    model = Fan
    template_name = 'fans/fan_confirm_delete.html'
    success_url = reverse_lazy('fans:list')
