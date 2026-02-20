from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Comment

class CommentCreateView(CreateView):
    model = Comment
    fields = ['text', 'fan', 'match']

    def form_valid(self, form):
        form.instance.match_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('matches:list')
