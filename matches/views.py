from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from matches.forms import MatchForm
from matches.models import Match


class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/match_create.html'
    success_url = reverse_lazy('matches:list')

    def form_valid(self, form):
        messages.success(self.request, 'Match successfully created!')
        return super().form_valid(form)



class MatchListView(ListView):
    model = Match
    template_name = 'matches/match_list.html'
    context_object_name = 'matches'



class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/match_update.html'
    success_url = reverse_lazy('matches:list')

    def form_valid(self, form):
        messages.success(self.request, 'Match successfully updated!')
        return super().form_valid(form)



class MatchDeleteView(DeleteView):
    model = Match
    template_name = 'matches/match_confirm_delete.html'
    success_url = reverse_lazy('matches:list')
