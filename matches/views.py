from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from matches.models import Match
from .serializers import MatchSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .tasks import capitalize_opponent_match_teams
from celery.exceptions import CeleryError

from matches.forms import MatchForm
from matches.models import Match

class MatchPermissionsRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.has_perm('matches.add_match') or \
               user.has_perm('matches.change_match') or \
               user.has_perm('matches.delete_match')

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to access Match management.")
        raise PermissionDenied

class MatchCreateView(LoginRequiredMixin, MatchPermissionsRequiredMixin,CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/match_create.html'
    success_url = reverse_lazy('matches:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            capitalize_opponent_match_teams.delay(self.object.id)
        except CeleryError as exc:
            print(f"Celery task could not be sent: {exc}")

        messages.success(self.request, 'Match successfully created!')
        return response



class MatchListView(LoginRequiredMixin,ListView):
    model = Match
    template_name = 'matches/match_list.html'
    context_object_name = 'matches'



class MatchUpdateView(LoginRequiredMixin, MatchPermissionsRequiredMixin,UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/match_update.html'
    success_url = reverse_lazy('matches:list')

    def form_valid(self, form):
        messages.success(self.request, 'Match successfully updated!')
        return super().form_valid(form)



class MatchDeleteView(LoginRequiredMixin, MatchPermissionsRequiredMixin,DeleteView):
    model = Match
    template_name = 'matches/match_confirm_delete.html'
    success_url = reverse_lazy('matches:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        match = self.object

        context['readonly_data'] = {
            "Date": match.date,
            "Opponent": match.opponent_team,
            "Score": f"{match.score_goal_real_madrid} - {match.score_goal_opponent}",
            "Stadium": match.stadium,
            "Referee": match.referee,
        }

        return context


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]