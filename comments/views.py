from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CommentForm
from .models import Comment

class CommentCreateView(CreateView):
    model = Comment
    template_name = "comments/comment_form.html"
    form_class = CommentForm
    success_url = reverse_lazy('matches:list')

