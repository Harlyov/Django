from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

from fans.forms import FanForm
from fans.models import Fan


class FanPermissionsRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.request.user
        return user.has_perm('fans.add_fan') or \
               user.has_perm('fans.change_fan') or \
               user.has_perm('fans.delete_fan')

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to access Fan management.")
        raise PermissionDenied

class FanCreateView(LoginRequiredMixin, FanPermissionsRequiredMixin,CreateView):
    model = Fan
    form_class = FanForm
    template_name = 'fans/fan_create.html'
    success_url = reverse_lazy('fans:list')

    def form_valid(self, form):
        messages.success(self.request, 'Fan successfully created!')
        return super().form_valid(form)


class FanUpdateView(LoginRequiredMixin, FanPermissionsRequiredMixin,UpdateView):
    model = Fan
    form_class = FanForm
    template_name = 'fans/fan_update.html'
    success_url = reverse_lazy('fans:list')

    def form_valid(self, form):
        messages.success(self.request, 'Fan successfully updated!')
        return super().form_valid(form)


class FanListView(LoginRequiredMixin,ListView):
    model = Fan
    template_name = 'fans/fan_list.html'
    context_object_name = 'fans'


class FanDeleteView(LoginRequiredMixin, FanPermissionsRequiredMixin,DeleteView):
    model = Fan
    template_name = 'fans/fan_confirm_delete.html'
    success_url = reverse_lazy('fans:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fan = self.object
        context['readonly_data'] = {
            "Name": fan.name,
            "Location": fan.location,
            "Favourite Player": fan.favourite_player.name,
        }
        return context