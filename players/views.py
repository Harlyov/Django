from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from players.forms import PlayerForm
from players.models import Player


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('players:list')

    def form_valid(self, form):
        messages.success(self.request, 'Player successfully created')
        return super().form_valid(form)


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_update.html'
    success_url = reverse_lazy('players:list')


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'
    success_url = reverse_lazy('players:list')




class PlayerListView(ListView):
    model = Player
    template_name = 'players/players_list.html'
    context_object_name = 'players'
