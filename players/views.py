from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from players.forms import PlayerForm
from players.models import Player


class PlayerPermissionsRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.has_perm('players.add_player') or \
               user.has_perm('players.change_player') or \
               user.has_perm('players.delete_player')

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to access Player management.")
        raise PermissionDenied

class PlayerCreateView(LoginRequiredMixin, PlayerPermissionsRequiredMixin,CreateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('players:list')

    def form_valid(self, form):
        messages.success(self.request, 'Player successfully created')
        return super().form_valid(form)


class PlayerUpdateView(LoginRequiredMixin, PlayerPermissionsRequiredMixin,UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_update.html'
    success_url = reverse_lazy('players:list')


class PlayerDeleteView(LoginRequiredMixin, PlayerPermissionsRequiredMixin,DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'
    success_url = reverse_lazy('players:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.object
        context['readonly_data'] = {
            "Name": player.name,
            "Position": player.position,
            "Shirt Number": player.shirt_number,
            "Age": player.age,
            "Photo URL": player.photo_url if player.photo_url else "No Image",
        }
        return context



class PlayerListView(LoginRequiredMixin,ListView):
    model = Player
    template_name = 'players/players_list.html'
    context_object_name = 'players'
